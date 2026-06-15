#!/usr/bin/env python3
"""Convert PRECISE-1K (expression matrix + metadata) -> a DE table + perturbation map.

This is the host-side adapter the headline experiment needs: it feeds
``scripts/benchmark_expression.py`` (which scores the simulator's predicted gene
directions against MEASURED differential expression, with the conflict subset as
the LLM-vs-rules battleground).

It targets the clean single-gene knockout conditions in PRECISE-1K, named
``[bw_]del<gene>_<media>`` (e.g. delcrp_glc, bw_delcra_glc), each matched to the
WT control on the SAME background+media (``wt_<media>`` / ``bw_<media>``). For
each KO it computes per-gene log2FC = mean(KO) - mean(control) (the matrix is
already log2-TPM) and a Welch z-approximation p-value, BH-adjusted within the
perturbation (no scipy on the host, so the test is approximate — documented, not
hidden).

    python scripts/precise1k_to_de.py \
        --matrix data/raw/precise1k/log_tpm_qc.csv \
        --metadata data/raw/precise1k/metadata_qc.csv \
        --out-de data/raw/precise1k/precise1k_de.tsv \
        --out-map data/raw/precise1k/precise1k_map.yaml
    python scripts/benchmark_expression.py \
        --expression data/raw/precise1k/precise1k_de.tsv \
        --map data/raw/precise1k/precise1k_map.yaml --mode both
"""
from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# [bw_] del [-_] <gene> _ <media...>   -- single-gene KOs only (skip multi-gene like delar1ar2)
KO_RE = re.compile(r"^(?P<bw>bw_)?del[-_]?(?P<gene>[A-Za-z][A-Za-z0-9]*)_(?P<media>.+)$")


def parse_args():
    p = argparse.ArgumentParser(description="PRECISE-1K -> DE table + perturbation map.")
    p.add_argument("--matrix", type=Path, required=True, help="log2-TPM matrix (genes x samples)")
    p.add_argument("--metadata", type=Path, required=True)
    p.add_argument("--out-de", type=Path, required=True)
    p.add_argument("--out-map", type=Path, required=True)
    p.add_argument("--min-reps", type=int, default=2, help="min replicates required in BOTH KO and control")
    p.add_argument("--min-lfc-emit", type=float, default=0.25, help="only emit DE rows with |log2fc| >= this")
    return p.parse_args()


def bh_adjust(pvals: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg FDR. Returns padj aligned to the input order."""
    n = len(pvals)
    if n == 0:
        return pvals
    order = np.argsort(pvals)
    ranked = pvals[order]
    adj = ranked * n / (np.arange(n) + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]  # enforce monotonicity from the top
    out = np.empty(n)
    out[order] = np.clip(adj, 0, 1)
    return out


def welch_z_p(ko: np.ndarray, wt: np.ndarray) -> tuple:
    """Per-gene log2fc + two-sided normal-approx p (Welch). Arrays: genes x reps."""
    m_ko, m_wt = ko.mean(1), wt.mean(1)
    lfc = m_ko - m_wt
    v_ko = ko.var(1, ddof=1) if ko.shape[1] > 1 else np.zeros(ko.shape[0])
    v_wt = wt.var(1, ddof=1) if wt.shape[1] > 1 else np.zeros(wt.shape[0])
    se = np.sqrt(v_ko / ko.shape[1] + v_wt / wt.shape[1])
    with np.errstate(divide="ignore", invalid="ignore"):
        z = np.where(se > 0, np.abs(lfc) / se, 0.0)
    p = np.array([math.erfc(zi / math.sqrt(2)) for zi in z])  # two-sided normal approx
    return lfc, p


def main() -> int:
    args = parse_args()
    expr = pd.read_csv(PROJECT_ROOT / args.matrix, index_col=0)
    meta = pd.read_csv(PROJECT_ROOT / args.metadata, index_col=0)
    # keep only metadata samples that exist as matrix columns
    cols = set(expr.columns)
    meta = meta[meta.index.isin(cols)]
    cond2samples = {c: list(g.index) for c, g in meta.groupby("condition")}

    de_rows = []
    pert_map_lines = ["# PRECISE-1K single-gene KO -> sim perturbation (auto-generated)"]
    used = []
    skipped = []
    for cond, samples in sorted(cond2samples.items()):
        m = KO_RE.match(cond)
        if not m:
            continue
        gene = m.group("gene").lower()
        media = m.group("media")
        ctrl_cond = ("bw_" if m.group("bw") else "wt_") + media
        ctrl = cond2samples.get(ctrl_cond)
        if not ctrl:
            skipped.append((cond, f"no control {ctrl_cond}"))
            continue
        if len(samples) < args.min_reps or len(ctrl) < args.min_reps:
            skipped.append((cond, f"too few reps (ko={len(samples)}, ctrl={len(ctrl)})"))
            continue
        ko = expr[samples].to_numpy()
        wt = expr[ctrl].to_numpy()
        lfc, p = welch_z_p(ko, wt)
        padj = bh_adjust(p)
        genes = expr.index.to_numpy()
        keep = np.abs(lfc) >= args.min_lfc_emit
        for g, l, pa in zip(genes[keep], lfc[keep], padj[keep]):
            de_rows.append((cond, str(g).lower(), f"{l:.4f}", f"{pa:.3e}"))
        pert_map_lines.append(f"{cond}: [{{entity: {gene}, state: inhibited}}]")
        used.append((cond, gene, ctrl_cond, len(samples), len(ctrl), int(keep.sum())))

    out_de = PROJECT_ROOT / args.out_de
    out_de.parent.mkdir(parents=True, exist_ok=True)
    with out_de.open("w", encoding="utf-8") as fh:
        fh.write("perturbation_id\tgene\tlog2fc\tpadj\n")
        for r in de_rows:
            fh.write("\t".join(r) + "\n")
    (PROJECT_ROOT / args.out_map).write_text("\n".join(pert_map_lines) + "\n", encoding="utf-8")

    print(f"perturbations: {len(used)}  DE rows: {len(de_rows)}  skipped: {len(skipped)}")
    for cond, gene, ctrl, nko, nwt, ndeg in used:
        print(f"  {cond:22s} gene={gene:8s} ctrl={ctrl:10s} ko={nko} wt={nwt} emitted={ndeg}")
    if skipped:
        print("skipped (first 10):")
        for c, why in skipped[:10]:
            print(f"  {c}: {why}")
    print(f"\nwrote {out_de}\nwrote {PROJECT_ROOT / args.out_map}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
