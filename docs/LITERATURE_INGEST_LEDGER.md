# Literature edge ingest ledger

Source: `/Users/ycy/Desktop/e.coil/data/literature/regulatory_edges.jsonl` (13 curated edges)  ·  graph: `data/normalized/simulation`
RegulonDB gold: `NetworkRegulatorGene.tsv` (FROZEN, read-only — used only to flag overlap).

## Summary

| Category | n | meaning |
| --- | --- | --- |
| ADD | 4 | eligible new hard edges -> overlay (separate file, NOT in edges.csv) |
| ALREADY_IN_GRAPH_CONFIRM | 5 | literature agrees with an edge already present |
| CONFLICT | 1 | literature direction != graph; flagged for human, NOT changed |
| GATED_OUT | 1 | preprint / review / omics / non-K12 -> not a hard edge |
| ID_MISMATCH | 0 | stated b-number/UniProt disagrees with the name -> flagged, not guessed (rule 4) |
| UNRESOLVED | 2 | endpoint id not in KG canonical set -> not guessed |

**Circularity guard:** of 4 ADDed edges, **1 already exist in RegulonDB** and 3 are NOVEL. Because the overlay is a separate file, KG-recall validation (validate_kg.py on edges.csv) never sees these, so recall is not inflated.

## Per-edge ledger

| Category | Edge | Paper | Tier | Detail |
| --- | --- | --- | --- | --- |
| ADD | RecA->LexA (represses) | Cory 2024 Nat Struct Mol Biol | direct/K-12 | protein.P0A7G6->gene.b4043 represses; novel_vs_regulondb=True |
| ADD | LexA->sulA (represses) | Cory 2024 Nat Struct Mol Biol | direct/K-12 | protein.P0A7C2->gene.b0958 represses; novel_vs_regulondb=False |
| ADD | IbpA->rpoH (represses) | Miwa & Taguchi 2023 PNAS | direct/K-12 | protein.P0C054->gene.b3461 represses; novel_vs_regulondb=True |
| ADD | RssB->rpoS (represses) | Bouillet 2024 PLoS Genet | direct/K-12 | protein.P0AEV1->gene.b2741 represses; novel_vs_regulondb=True |
| CONFLICT | CRP->lacI (represses) | Lin 2025 bioRxiv | direct/preprint/K-12 | protein.P0ACJ8->gene.b0345: graph=activates vs lit=represses; gold=True (NOT changed) |
| ALREADY_IN_GRAPH_CONFIRM | CsrA->gadA (represses) | Gorelik 2024 J Bacteriol | direct/K-12 | protein.P69913->gene.b3517 represses; gold=True |
| ALREADY_IN_GRAPH_CONFIRM | CsrA->gadB (represses) | Gorelik 2024 J Bacteriol | direct/K-12 | protein.P69913->gene.b1493 represses; gold=True |
| ALREADY_IN_GRAPH_CONFIRM | CsrA->ydeO (represses) | Gorelik 2024 J Bacteriol | direct/K-12 | protein.P69913->gene.b1499 represses; gold=True |
| ALREADY_IN_GRAPH_CONFIRM | Cra->pfkA (represses) | Huang 2024 Appl Environ Microbiol | review/K-12 | protein.P0ACP1->gene.b3916 represses; gold=True |
| ALREADY_IN_GRAPH_CONFIRM | RpoS->rssB (activates) | Bouillet 2024 PLoS Genet | direct/K-12 | protein.P13445->gene.b1235 activates; gold=False |
| GATED_OUT | H-NS->ompF (represses) | Chen 2025 Front Vet Sci | direct/ATCC-25922 | protein.P0ACF8->gene.b0929 represses; strain=ATCC-25922; gold=False |
| UNRESOLVED | GcvB->sodB (represses) | Barsheshet Vigoda 2024 NAR | direct/K-12 | regulator=unresolved target=name:gene |
| UNRESOLVED | OmrA->btuB (represses) | Bastet 2024 NAR | direct/K-12 | regulator=unresolved target=name:gene |
