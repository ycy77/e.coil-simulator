#!/usr/bin/env python3
"""Validate the graph's regulatory edges against an independent expression compendium.

This is an EXTERNAL check that does not reuse RegulonDB: if the graph says TF X
*activates* gene Y, then across a large, heterogeneous expression compendium X
and Y should tend to be positively correlated; *represses* should tend negative.
Using the Tjaden 2023 compendium (3,376 RNA-seq samples), we measure whether the
graph's regulatory signs agree with co-expression — a quantitative,
reviewer-grade signal that the regulatory layer is real, not just internally
consistent.

    # after scripts/fetch_transcriptome_compendium.py
    python scripts/validate_coexpression.py --matrix data/raw/transcriptome_compendium/<expr.tsv>

The matrix loader auto-detects orientation (genes as rows vs columns) and id
column; override with --gene-col / --orient / --delimiter if needed.

Outputs docs/COEXPRESSION_VALIDATION.md + a summary. The correlation and loader
helpers are unit-tested offline (tests/test_coexpression.py) on a synthetic
matrix; the real numbers come from running it on the fetched data.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.graph import StaticGraph  # noqa: E402


def pearson(x: List[float], y: List[float]) -> Optional[float]:
    n = len(x)
    if n < 3:
        return None
    mx = sum(x) / n
    my = sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    if sxx <= 0 or syy <= 0:
        return None
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    return sxy / math.sqrt(sxx * syy)


def _sniff_delim(header: str) -> str:
    return "\t" if header.count("\t") >= header.count(",") else ","


def load_matrix(path: Path, delimiter: str = "", gene_col: int = 0,
                orient: str = "auto", log: bool = True,
                wanted_keys: Optional[set] = None) -> Dict[str, List[float]]:
    """Return {gene_key_lower: [expression across samples]}.

    ``wanted_keys`` (lowercased gene ids/names) restricts what is kept, bounding
    memory on a large matrix. ``orient='rows'`` = genes are rows (default guess),
    ``'cols'`` = genes are columns (matrix is transposed).
    """
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not text:
        return {}
    delim = delimiter or _sniff_delim(text[0])
    rows = [line.split(delim) for line in text if line.strip()]
    header = rows[0]

    if orient == "auto":
        # genes-as-rows if the first column of body rows looks like gene ids
        sample_ids = [r[gene_col].strip().lower() for r in rows[1:50] if len(r) > gene_col]
        orient = "rows"
        if wanted_keys and sample_ids:
            hit_rows = sum(1 for s in sample_ids if s in wanted_keys)
            hdr_keys = [h.strip().lower() for h in header[1:]]
            hit_cols = sum(1 for h in hdr_keys[:200] if h in wanted_keys)
            orient = "cols" if hit_cols > hit_rows else "rows"

    out: Dict[str, List[float]] = {}

    def _to_float(v: str) -> float:
        try:
            f = float(v)
        except ValueError:
            f = 0.0
        return math.log1p(f) if log else f

    if orient == "cols":
        gene_keys = [h.strip().lower() for h in header[1:]]
        cols = {k: [] for k in gene_keys if (wanted_keys is None or k in wanted_keys)}
        keep_idx = {i: k for i, k in enumerate(gene_keys) if k in cols}
        for r in rows[1:]:
            vals = r[1:]
            for i, k in keep_idx.items():
                cols[k].append(_to_float(vals[i]) if i < len(vals) else 0.0)
        return cols

    for r in rows[1:]:
        if len(r) <= gene_col:
            continue
        key = r[gene_col].strip().lower()
        if wanted_keys is not None and key not in wanted_keys:
            continue
        vals = [c for j, c in enumerate(r) if j != gene_col]
        out[key] = [_to_float(v) for v in vals]
    return out


def entity_expression_key(graph: StaticGraph, entity_id: str, expr: Dict[str, List[float]]):
    """Resolve a graph entity to an expression vector via its name/aliases/b-number.

    A regulator protein's expression is that of its encoding gene, whose b-number
    and symbol are in the protein's aliases, so name/alias lookup suffices.
    """
    ent = graph.entities.get(entity_id)
    if not ent:
        return None
    for key in [ent.name] + list(ent.aliases):
        k = key.strip().lower()
        if k in expr:
            return expr[k]
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Co-expression validation of regulatory edges.")
    ap.add_argument("--graph", type=Path, default=Path("data/normalized/simulation"))
    ap.add_argument("--matrix", type=Path, required=True)
    ap.add_argument("--delimiter", default="")
    ap.add_argument("--gene-col", type=int, default=0)
    ap.add_argument("--orient", choices=("auto", "rows", "cols"), default="auto")
    ap.add_argument("--no-log", action="store_true")
    ap.add_argument("--strong", type=float, default=0.3, help="|r| threshold for a 'strong' call")
    args = ap.parse_args()

    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / args.graph)
    reg_edges = [(e.source_id, e.target_id, e.relation_type)
                 for e in graph.edges if e.relation_type in ("activates", "represses")]

    # which gene keys do we need (to bound matrix memory)
    wanted = set()
    for s, t, _ in reg_edges:
        for eid in (s, t):
            ent = graph.entities.get(eid)
            if ent:
                for key in [ent.name] + list(ent.aliases):
                    wanted.add(key.strip().lower())

    expr = load_matrix(PROJECT_ROOT / args.matrix, args.delimiter, args.gene_col,
                       args.orient, log=not args.no_log, wanted_keys=wanted)
    n_samples = len(next(iter(expr.values()))) if expr else 0
    print(f"loaded expression for {len(expr)} gene keys x {n_samples} samples")

    by_sign = defaultdict(list)  # relation -> list of correlations
    scored = 0
    for s, t, rel in reg_edges:
        xs = entity_expression_key(graph, s, expr)
        ys = entity_expression_key(graph, t, expr)
        if xs is None or ys is None or len(xs) != len(ys):
            continue
        r = pearson(xs, ys)
        if r is None:
            continue
        by_sign[rel].append(r)
        scored += 1

    def stats(vals):
        if not vals:
            return {"n": 0}
        m = sum(vals) / len(vals)
        pos = sum(1 for v in vals if v > 0) / len(vals)
        strong = sum(1 for v in vals if abs(v) >= args.strong) / len(vals)
        return {"n": len(vals), "mean_r": round(m, 3), "frac_positive": round(pos, 3),
                "frac_strong": round(strong, 3)}

    act = stats(by_sign["activates"])
    rep = stats(by_sign["represses"])
    # sign agreement: activates expected r>0, represses expected r<0
    agree = sum(1 for v in by_sign["activates"] if v > 0) + sum(1 for v in by_sign["represses"] if v < 0)
    sign_acc = round(agree / scored, 3) if scored else None

    lines = [
        f"# Co-expression validation of regulatory edges ({args.graph})",
        "",
        f"External data: Tjaden 2023 compendium — {n_samples} samples, "
        f"{len(expr)} mapped gene keys.",
        f"Regulatory edges scored (both endpoints have expression): **{scored}** / {len(reg_edges)}.",
        "",
        "## Correlation by regulatory sign",
        "",
        "| Sign | n | mean r | frac r>0 | frac |r|≥{:.1f} |".format(args.strong),
        "| --- | --- | --- | --- | --- |",
        f"| activates (expect r>0) | {act.get('n')} | {act.get('mean_r')} | {act.get('frac_positive')} | {act.get('frac_strong')} |",
        f"| represses (expect r<0) | {rep.get('n')} | {rep.get('mean_r')} | {rep.get('frac_positive')} | {rep.get('frac_strong')} |",
        "",
        f"**Sign agreement with co-expression: {sign_acc} ({agree}/{scored})** "
        "(activates↔r>0, represses↔r<0).",
        "",
        "## Interpretation",
        "",
        "- activates mean_r should be clearly above represses mean_r; ideally activates>0>represses.",
        "- This is independent of RegulonDB (expression data, not curation), so agreement is genuine "
        "external validation of the graph's regulatory directions.",
        "- Edges with sign opposite to a strong correlation are data-quality candidates to review.",
    ]
    report = "\n".join(lines) + "\n"
    out = PROJECT_ROOT / "docs" / "COEXPRESSION_VALIDATION.md"
    out.write_text(report, encoding="utf-8")
    print(report)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
