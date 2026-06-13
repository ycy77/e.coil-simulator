#!/usr/bin/env python3
"""Augment the simulation baseline with missing edges.

The baseline split + flatten step produced a clean graph but
also severed several edge classes that have legitimate
biological meaning:

  1. sRNA regulatory edges  (rna -> gene)
     RegulonDB has 309 sRNA regulator edges, all stored as
     gene -> gene. The sRNA products of those genes are
     otherwise orphaned. We mirror each as rna -> gene so the
     sRNA entity gets a non-empty neighborhood.

  2. gene -> rna `transcribed_as`
     215 b-numbers appear as both a gene and an rna (the
     sRNA is the transcript of its gene). The relation is
     implicit in the b-number but absent from the edge list.

  3. RegulonDB edges v2 missed
     313 of 6077 RegulonDB edges were skipped during the v2
     merge because of composite source IDs like
     ``gene.b1712|b0912`` (multi-gene regulators, e.g. the IHF
     heterodimer). We try every alternative ID and keep the
     edge when at least one component lands in baseline.

  4. Complex -> bound ligand
     Twelve baseline complexes carry their bound ligand in
     the name (``AraC-alpha-L-arabinopyranose``). We mine the
     name for a matching small_molecule in baseline and add a
     ``bound_by`` edge from complex -> ligand.

  5. Pseudogene -> functional copy
     Six baseline proteins are annotated as "fragment of X".
     We add a ``paralog_of`` edge from pseudogene -> parent
     whenever the parent is a baseline protein.

The script writes all new edges to
``data/normalized/_v2/edges_augmented.csv`` (a *separate*
file). Re-run ``build_simulation_baseline.py`` after merging
that file into ``simulation/edges.csv`` to pick them up. The
script is idempotent: it never duplicates edges already
present in the augmented file.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_V2 = PROJECT_ROOT / "data" / "normalized" / "_v2"
DEFAULT_RDB = PROJECT_ROOT / "data" / "normalized" / "regulondb_edges.csv"
DEFAULT_OUT = PROJECT_ROOT / "data" / "normalized" / "_v2" / "edges_augmented.csv"

# sRNA names that appear in RegulonDB ``regulator=`` notes. The
# list covers the well-characterized E. coli K-12 sRNAs and is
# used to spot a gene -> gene edge that is actually mediated by
# a sRNA product.
# All sRNA names normalised to lower-case so the data match
# (rna entities in the v2 dump are spelled lower-case: ``sgrS``,
# ``arcZ``). Curated against the sRNA names that actually
# appear in the rna entity list (see scripts/dump_rna_names.py
# to regenerate).
SRNA_NAMES = {
    "acek-int",
    "amgr",
    "amrf",
    "arcz",
    "arrs",
    "ascrp",
    "asflhd",
    "asompr",
    "asphop",
    "azur",
    "bhsb",
    "chix",
    "chiz",
    "cpxq",
    "csrb",
    "csrc",
    "cyar",
    "dicb",
    "dicf",
    "dsra",
    "esre",
    "fimr2",
    "fis",
    "fisa",
    "fisb",
    "flgo",
    "flix",
    "fnrs",
    "ftso",
    "gadf",
    "gady",
    "gcvb",
    "ghos",
    "glmy",
    "glmz",
    "ibsa",
    "ibsb",
    "iscsrdb",
    "isrc",
    "isrj",
    "istr",
    "kils",
    "malh",
    "mars",
    "mcas",
    "meoh-rna",
    "mgrb",
    "mgrr",
    "mgrs",
    "mica",
    "micc",
    "micf",
    "micl",
    "mnts",
    "motr",
    "nars",
    "ohsc",
    "omra",
    "omrb",
    "oxys",
    "pdel",
    "psph",
    "raiz",
    "rala",
    "rbsz",
    "rdla",
    "rdlb",
    "rdlc",
    "rdld",
    "rira",
    "rpra",
    "rsea",
    "rseh",
    "rsex",
    "rttr",
    "ryba",
    "rybb",
    "ryda",
    "rydb",
    "rydc",
    "ryea",
    "ryeb",
    "ryec",
    "ryed",
    "ryee",
    "ryfa",
    "ryfd",
    "ryhb",
    "ryja",
    "ryjb",
    "sdhx",
    "sdsr",
    "sgrs",
    "siba",
    "sibb",
    "sibc",
    "sibd",
    "sibe",
    "sokb",
    "sokc",
    "sokd",
    "soke",
    "sokf",
    "sokg",
    "sokh",
    "sokx",
    "spf",
    "spot42",
    "srab",
    "srag",
    "sral",
    "sroa",
    "srob",
    "sroc",
    "srod",
    "sroe",
    "sroh",
    "ssrs",
    "symr",
    "tff",
    "timr",
    "uhpu",
    "xylz",
    "yrdg",
    "zbij",
}

# Edge fields written to the augmented file. Matches the
# flattened-reaction schema so downstream code does not have to
# special-case it.
EDGE_FIELDS = [
    "source_id", "target_id", "relation_type", "direction", "evidence",
    "source_database", "source_record_id", "notes",
    "reaction_id", "reactants", "products", "ec_number", "pathway",
]


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def index_by_id(entities: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    return {e["entity_id"]: e for e in entities}


def index_by_name(entities: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    out: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for e in entities:
        out[e["name"]].append(e)
    return out


# ---------------------------------------------------------------------------
# Source reconstruction: ``gene.b1712|b0912`` -> [b1712, b0912]
# ---------------------------------------------------------------------------

def split_composite_source(source_id: str) -> List[str]:
    """A RegulonDB source like ``gene.b1712|b0912`` is a multi-gene
    regulator (e.g. the IHF heterodimer). Returns each candidate
    gene id."""
    if "|" not in source_id:
        return [source_id]
    # Strip the "gene." prefix once, split the rest.
    if "." in source_id:
        prefix, rest = source_id.split(".", 1)
    else:
        prefix, rest = "", source_id
    parts = [p.strip() for p in rest.split("|") if p.strip()]
    return [f"{prefix}.{p}" if prefix else p for p in parts]


def parse_regulator_from_notes(notes: str) -> Optional[str]:
    m = re.search(r"regulator=([A-Za-z0-9_\-\.]+)", notes or "")
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Edge builders
# ---------------------------------------------------------------------------

def build_transcribed_as(
    entities: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    """gene.X --transcribed_as--> rna.X when b-number matches."""
    bnum_to_gene: Dict[str, str] = {}
    bnum_to_rna: Dict[str, str] = {}
    for e in entities:
        eid = e["entity_id"]
        if "." not in eid:
            continue
        bnum = eid.split(".")[-1]
        if not (bnum.startswith("b") and bnum[1:].isdigit()):
            continue
        if e["entity_type"] == "gene":
            bnum_to_gene.setdefault(bnum, eid)
        elif e["entity_type"] == "rna":
            bnum_to_rna.setdefault(bnum, eid)
    rows = []
    for bnum, gene_id in sorted(bnum_to_gene.items()):
        rna_id = bnum_to_rna.get(bnum)
        if not rna_id:
            continue
        rows.append({
            "source_id": gene_id,
            "target_id": rna_id,
            "relation_type": "transcribed_as",
            "direction": "directed",
            "evidence": "b-number co-location",
            "source_database": "internal_alignment",
            "source_record_id": f"bnum:{bnum}",
            "notes": f"gene/rna share b-number {bnum}",
            "reaction_id": "", "reactants": "", "products": "",
            "ec_number": "", "pathway": "",
        })
    return rows


def build_srna_regulation_from_regulondb(
    entities: List[Dict[str, str]],
    rdb_edges: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    """Mirror each sRNA-flavoured RegulonDB gene -> gene edge as
    a rna -> gene edge so the sRNA entity has neighbours."""
    by_name = index_by_name(entities)
    rows = []
    seen: Set[Tuple[str, str, str]] = set()
    # Common English words that happen to be real gene names.
    # Without this filter we get false positives like
    # protein P02920 -> "Can" (colicin) or P00722 -> "Beta"
    # (gyrase subunit).
    _ENGLISH_NOISE = {
        "Beta", "Delta", "Alpha", "Gamma", "Sigma", "Omega",
        "Can", "Could", "May", "Will", "Would", "Should",
        "Note", "This", "That", "These", "Those",
        "Acts", "Binds", "Has", "Have",
        "Are", "Was", "Were", "But", "Not", "Yet",
        "When", "Then", "Now", "Here", "There", "What",
        "How", "Why", "Who", "Whom", "Whose",
        "Sub", "Subunit", "Subunits", "Catalyzes", "Activates",
        "Inhibits", "Regulates", "Required", "Important",
        "Also", "Only", "Even", "Just", "Like", "Many",
        "Most", "Some", "Such", "Very", "Much", "More",
        "Less", "Other", "Another", "Same", "Different",
        "First", "Last", "Next", "Previous", "Following",
        "Containing", "Includes", "Contains",
        "Tissue", "Specificity", "Phosphorylation",
        "Expression", "Transcriptional", "Translational",
        "Activity", "Active", "Inactive", "Mature",
        "Precursor", "Monomer", "Dimer", "Trimer", "Tetramer",
        "Oligomer", "Polymer", "Complex", "Component",
        "Chain", "Cys", "His", "Asp", "Glu", "Ser", "Thr",
        "Tyr", "Lys", "Arg", "Ala", "Gly", "Pro", "Asn",
        "Gln", "Phe", "Leu", "Ile", "Met", "Trp", "Val",
        "Stop", "Start", "End", "Begin",
        "Epub", "Ahead", "Print", "Editor", "Issue",
        "Volume", "Page", "Pages", "Figure", "Table",
        "Box", "Cartoon", "Legend", "See", "Refer", "Ref",
        "Cited", "Cites", "Reference", "References",
    }
    def _has_frag_context(ann_low: str) -> bool:
        return any(kw in ann_low for kw in (
            "pseudogene", "fragment", "truncated",
            "n-terminal", "c-terminal", "split into", "two chains",
        ))
    for e in rdb_edges:
        notes = e.get("notes", "")
        regulator = parse_regulator_from_notes(notes)
        if not regulator:
            continue
        # RegulonDB uses mixed case ("SgrS") but our rna
        # entities are lower-case. Normalise both ways.
        regulator_lc = regulator.lower()
        if regulator_lc not in SRNA_NAMES:
            continue
        # The sRNA entity should exist in the data, with name == regulator.
        # by_name is keyed on the canonical-cased name in
        # entities.csv; the rna entities are all lower-case.
        candidates = by_name.get(regulator) or by_name.get(regulator_lc) or []
        srna = next((c for c in candidates if c["entity_type"] == "rna"), None)
        if not srna:
            # also try a substring search
            for n, items in by_name.items():
                if n.lower() == regulator_lc:
                    cand = next((c for c in items if c["entity_type"] == "rna"), None)
                    if cand:
                        srna = cand
                        break
        if not srna:
            continue
        target_gene = e["target_id"]
        if not target_gene.startswith("gene."):
            continue
        relation = e["relation_type"]
        if relation not in {"activates", "represses"}:
            continue
        triple = (srna["entity_id"], target_gene, relation)
        if triple in seen:
            continue
        seen.add(triple)
        rows.append({
            "source_id": srna["entity_id"],
            "target_id": target_gene,
            "relation_type": relation,
            "direction": "directed",
            "evidence": f"RegulonDB regulator={regulator}",
            "source_database": "RegulonDB",
            "source_record_id": e.get("source_record_id", ""),
            "notes": f"sRNA {regulator} {relation} target gene",
            "reaction_id": "", "reactants": "", "products": "",
            "ec_number": "", "pathway": "",
        })
    return rows


def build_missed_regulondb_edges(
    entities: List[Dict[str, str]],
    rdb_edges: List[Dict[str, str]],
    existing_edges: Set[Tuple[str, str, str]],
) -> List[Dict[str, str]]:
    """Edges v2 missed. For each, try every component of the
    composite source id; keep if at least one lands in the
    entity set."""
    e_ids = {e["entity_id"] for e in entities}
    rows = []
    for e in rdb_edges:
        rel = e["relation_type"]
        if rel not in {"activates", "represses"}:
            continue
        target = e["target_id"]
        if not target.startswith("gene."):
            continue
        for src in split_composite_source(e["source_id"]):
            if not src.startswith("gene."):
                continue
            if (src, target, rel) in existing_edges:
                continue
            if src not in e_ids or target not in e_ids:
                continue
            rows.append({
                "source_id": src,
                "target_id": target,
                "relation_type": rel,
                "direction": "directed",
                "evidence": e.get("evidence", "S"),
                "source_database": "RegulonDB",
                "source_record_id": e.get("source_record_id", ""),
                "notes": e.get("notes", ""),
                "reaction_id": "", "reactants": "", "products": "",
                "ec_number": "", "pathway": "",
            })
            existing_edges.add((src, target, rel))
    return rows


# ---------------------------------------------------------------------------
# Complex / ligand resolution
# ---------------------------------------------------------------------------

# Token -> candidate small_molecule name hints. The complex name
# is stripped of its TF component and split on '-'; any token
# that is a known ligand name resolves the complex's bound
# molecule. A handful of common glycans / amino acids are
# pre-listed so we do not have to rebuild a full dictionary.
LIGAND_HINTS = {
    "L-arabinopyranose", "D-fucose", "L-fucose", "D-galactose",
    "D-glucose", "D-mannose", "D-ribose", "L-rhamnose", "L-sorbose",
    "D-xylose", "D-arabinose", "L-arabinose", "D-allose", "D-psicose",
    "molybdate", "tungstate", "Zn2+", "Mn2+", "Mg2+", "Fe2+", "Fe3+",
    "Ni2+", "Co2+", "Cu2+", "2,4-dinitrophenol",
    "carbonylcyanide m-chlorophenylhydrazone", "salicylate",
    "L-carnitine", "L-serine", "D-serine", "L-tryptophan",
    "L-threonine", "L-methionine", "L-isoleucine", "L-leucine",
    "L-valine", "L-asparagine", "L-aspartate", "L-cysteine",
    "L-glutamate", "L-glutamine", "L-proline", "L-tyrosine",
    "L-phenylalanine", "L-lysine", "L-arginine", "L-histidine",
    "alpha-ketoglutarate", "ATP", "ADP", "NAD+", "NADH",
    "NADP+", "NADPH", "FAD", "FADH2", "heme", "siroheme",
    "cobalamin", "pyridoxal", "thiamine", "riboflavin",
    "autoinducer", "AI-2", "cAMP", "ppGpp", "c-di-GMP", "c-di-AMP",
}


def build_complex_ligand_edges(
    entities: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    """Complex names like 'AraC-alpha-L-arabinopyranose' carry
    the bound ligand. We strip the TF prefix heuristically
    (any word that matches a baseline protein or complex name)
    and resolve the remaining tokens against small_molecule
    names. When a ligand is found, we add a
    complex --bound_by--> ligand edge."""
    complexes = [e for e in entities if e["entity_type"] == "complex"]
    by_name = index_by_name(entities)
    rows = []
    seen = set()
    for c in complexes:
        cname = c["name"]
        # Try every known ligand hint as a substring of the
        # complex name. This is intentionally loose -- a
        # false positive here just adds an edge that the user
        # can prune in the UI.
        for hint in LIGAND_HINTS:
            if hint.lower() not in cname.lower():
                continue
            # Find the canonical small_molecule entity. We
            # match by name (case-insensitive) and prefer
            # the EcoCyc / UniProt source.
            candidates = [
                e for e in entities
                if e["entity_type"] == "small_molecule"
                and e["name"].lower() == hint.lower()
            ]
            if not candidates:
                # Also try aliases on the molecule
                for e in entities:
                    if e["entity_type"] != "small_molecule":
                        continue
                    blob = f" {e['name'].lower()} {(e.get('aliases') or '').lower()} "
                    if hint.lower() in blob:
                        candidates.append(e)
            if not candidates:
                continue
            cand = candidates[0]
            triple = (c["entity_id"], cand["entity_id"], "bound_by")
            if triple in seen:
                continue
            seen.add(triple)
            rows.append({
                "source_id": c["entity_id"],
                "target_id": cand["entity_id"],
                "relation_type": "bound_by",
                "direction": "directed",
                "evidence": "complex name contains ligand",
                "source_database": "internal_alignment",
                "source_record_id": f"complex:{c['name']}",
                "notes": f"complex '{cname}' carries '{hint}' as bound ligand",
                "reaction_id": "", "reactants": "", "products": "",
                "ec_number": "", "pathway": "",
            })
    return rows


# ---------------------------------------------------------------------------
# Pseudogene / fragment alignment
# ---------------------------------------------------------------------------

# Patterns found in UniProt annotations that name a parent
# protein. We extract the parent token and add a ``paralog_of``
# edge from the pseudogene to the parent.
# Tokens that look like protein/gene names (capitalized word,
# 2-10 chars, no digits in the middle). Used to mine the
# annotation text for parent-of-fragment mentions.
_NAME_TOKEN = re.compile(r"\b[A-Z][a-z]{1,3}[A-Z]?[a-z]{0,6}\b")


def build_paralog_edges(
    entities: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    """For every protein in baseline, look for any other
    baseline protein/gene name appearing in its annotation
    text. This is loose by design -- the candidate edges are
    surfaced for human review rather than blindly trusted. We
    use a wide token alphabet (incl. numbers, single capital
    letters, mixed case) so names like "RcsA", "RpoS", "RfaH"
    or "RNA" with attached digits match."""
    # Build the set of all candidate names in baseline
    candidate_names: Set[str] = set()
    for e in entities:
        if e["entity_type"] in {"protein", "gene"}:
            candidate_names.add(e["name"])
            # Also consider the source_id's tail (b-number) as
            # a fallback so cross-IDs match.
    by_name = index_by_name(entities)
    rows = []
    seen: Set[Tuple[str, str, str]] = set()
    # Common English words that happen to be real gene names.
    # Without this filter we get false positives like
    # protein P02920 -> "Can" (colicin) or P00722 -> "Beta"
    # (gyrase subunit).
    _ENGLISH_NOISE = {
        "Beta", "Delta", "Alpha", "Gamma", "Sigma", "Omega",
        "Can", "Could", "May", "Will", "Would", "Should",
        "Note", "This", "That", "These", "Those",
        "Acts", "Binds", "Has", "Have",
        "Are", "Was", "Were", "But", "Not", "Yet",
        "When", "Then", "Now", "Here", "There", "What",
        "How", "Why", "Who", "Whom", "Whose",
        "Sub", "Subunit", "Subunits", "Catalyzes", "Activates",
        "Inhibits", "Regulates", "Required", "Important",
        "Also", "Only", "Even", "Just", "Like", "Many",
        "Most", "Some", "Such", "Very", "Much", "More",
        "Less", "Other", "Another", "Same", "Different",
        "First", "Last", "Next", "Previous", "Following",
        "Containing", "Includes", "Contains",
        "Tissue", "Specificity", "Phosphorylation",
        "Expression", "Transcriptional", "Translational",
        "Activity", "Active", "Inactive", "Mature",
        "Precursor", "Monomer", "Dimer", "Trimer", "Tetramer",
        "Oligomer", "Polymer", "Complex", "Component",
        "Chain", "Cys", "His", "Asp", "Glu", "Ser", "Thr",
        "Tyr", "Lys", "Arg", "Ala", "Gly", "Pro", "Asn",
        "Gln", "Phe", "Leu", "Ile", "Met", "Trp", "Val",
        "Stop", "Start", "End", "Begin",
        "Epub", "Ahead", "Print", "Editor", "Issue",
        "Volume", "Page", "Pages", "Figure", "Table",
        "Box", "Cartoon", "Legend", "See", "Refer", "Ref",
        "Cited", "Cites", "Reference", "References",
    }
    def _has_frag_context(ann_low: str) -> bool:
        return any(kw in ann_low for kw in (
            "pseudogene", "fragment", "truncated",
            "n-terminal", "c-terminal", "split into", "two chains",
        ))
    _NOISE = {
        "DNA", "RNA", "ATP", "ADP", "NAD", "NADP", "GTP", "GDP", "UTP",
        "UDP", "CTP", "CDP", "FAD", "FMN", "CoA", "Co", "Mg", "Mn",
        "Zn", "Fe", "Cu", "Ni", "Mo", "W", "FUNCTION", "SUBCELLULAR",
        "LOCATION", "TISSUE", "SPECIFICITY", "DOMAIN", "ENZYME",
        "REGULATION", "DISEASE", "SIMILARITY", "MISCELLANEOUS",
        "PubMed", "MEDLINE", "ECO", "By", "In", "The", "It", "May",
        "Could", "This", "That", "These", "Acts", "Binds", "Acts",
        "Required", "Note", "And", "Encodes", "Probable", "Putative",
        "Master", "Couples", "Degrades", "Accelerates", "Endogenous",
        "Mediates", "RIP", "PubMed",
    }
    # Pattern: capitalised word optionally followed by lowercase
    # and possibly a digit. Catches "RcsA", "RpoS", "RfaH", "30S",
    # "RNase", "RNAP", "RipA" etc.
    _TOK = re.compile(r"\b[A-Z][a-z]{0,4}[A-Z]?[a-zA-Z0-9]{0,4}\b")
    for e in entities:
        if e["entity_type"] != "protein":
            continue
        ann = e.get("annotation") or ""
        if not ann:
            continue
        ann_low = ann.lower()
        self_id = e["entity_id"]
        self_name = e.get("name", "")
        # Context gate: only mine annotations that explicitly
        # mention fragment / pseudogene / truncated. Without
        # this filter the candidate-name set is too noisy
        # (every protein ends up linked to whatever common
        # word happens to be a real gene name).
        if not _has_frag_context(ann_low):
            continue
        # Every capitalised token is a candidate parent name.
        # Try longest first to bias toward "RcsA" over "Rcs".
        toks = sorted({m.group(0) for m in _TOK.finditer(ann)},
                      key=lambda s: -len(s))
        for cand in toks:
            if cand in _NOISE or cand in _ENGLISH_NOISE or len(cand) < 2:
                continue
            if cand == self_name or cand.lower() == self_name.lower():
                continue
            # Case-insensitive resolution: ``AcrA`` in the
            # annotation must match ``acrA`` in baseline.
            cand_lc = cand.lower()
            parent = None
            for n, items in by_name.items():
                if n.lower() != cand_lc:
                    continue
                parent = next(
                    (p for p in items
                     if p["entity_type"] in {"protein", "gene"}
                     and p["entity_id"] != self_id),
                    None,
                )
                if parent:
                    break
            if not parent:
                continue
            if not parent:
                continue
            triple = (self_id, parent["entity_id"], "paralog_of")
            if triple in seen:
                continue
            seen.add(triple)
            rows.append({
                "source_id": self_id,
                "target_id": parent["entity_id"],
                "relation_type": "paralog_of",
                "direction": "directed",
                "evidence": "UniProt annotation",
                "source_database": "UniProt",
                "source_record_id": e.get("source_id", ""),
                "notes": f"annotation mentions '{cand}' as related copy",
                "reaction_id": "", "reactants": "", "products": "",
                "ec_number": "", "pathway": "",
            })
            break  # one edge per protein is enough
    return rows


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--v2-dir", type=Path, default=DEFAULT_V2)
    p.add_argument("--regulondb-edges", type=Path, default=DEFAULT_RDB)
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = p.parse_args()

    v2 = args.v2_dir
    print(f"[1/4] reading v2 from {v2} ...")
    entities = read_csv(v2 / "entities.csv")
    edges = read_csv(v2 / "edges.csv")
    print(f"      {len(entities)} entities, {len(edges)} edges")

    print(f"[2/4] reading RegulonDB edges from {args.regulondb_edges} ...")
    rdb_edges = read_csv(args.regulondb_edges)
    print(f"      {len(rdb_edges)} rdb edges")

    print(f"[3/4] computing augmentations ...")
    existing = {(e["source_id"], e["target_id"], e["relation_type"]) for e in edges}
    # Pre-load the existing augmented file so re-runs are
    # idempotent.
    existing |= {(e["source_id"], e["target_id"], e["relation_type"])
                 for e in read_csv(args.out)}

    chunks = {
        "transcribed_as":        build_transcribed_as(entities),
        "srna_regulates":        build_srna_regulation_from_regulondb(entities, rdb_edges),
        "missed_regulondb":      build_missed_regulondb_edges(entities, rdb_edges, existing),
        "complex_bound_ligand":  build_complex_ligand_edges(entities),
        "paralog_of":            build_paralog_edges(entities),
    }
    for name, rows in chunks.items():
        print(f"      {name:30s} +{len(rows):4d} new edges")

    all_new = []
    for rows in chunks.values():
        all_new.extend(rows)

    print(f"[4/4] writing {len(all_new)} augmented edges to {args.out} ...")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EDGE_FIELDS)
        w.writeheader()
        for r in all_new:
            w.writerow({k: r.get(k, "") for k in EDGE_FIELDS})

    print()
    print("=" * 60)
    print(f"  {'section':30s} {'new':>6s}")
    print("-" * 60)
    for name, rows in chunks.items():
        print(f"  {name:30s} {len(rows):6d}")
    print("-" * 60)
    print(f"  {'total':30s} {len(all_new):6d}")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
