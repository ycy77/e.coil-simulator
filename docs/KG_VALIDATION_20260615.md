# Knowledge-graph validation vs RegulonDB (data/normalized/simulation)

Gold standard: `/Users/ycy/Desktop/e.coil/data/regulationDB/NetworkRegulatorGene.tsv` — 7352 unique (regulator, target, sign) interactions.

## Coverage (recall)

- Regulators mappable to a graph entity: **95.1%** (6990/7352)
- Target genes mappable: **99.8%** (7334/7352)
- Both endpoints mappable: **94.9%** (6974/7352)
- **Interactions present as a graph edge: 58.8% of all gold (4325/7352); 62.0% of the mappable subset (4325/6974)**

### Recall by evidence tier (the honest read)

RegulonDB tags each interaction Strong (direct experiment) or Weak (inferred).
The graph import keeps Strong by default; Weak is excluded by design, so overall
recall is dragged down by Weak interactions we deliberately do not import.

- **Strong (S): 94.4% (2957/3134)** — this is the meaningful completeness number for high-confidence regulation.
- Weak (W): 12.2% (365/2991) — excluded by default; run `build_regulondb_edges.py --include-weak` to add them (tagged).

## Sign accuracy (precision of direction)

- Graph edges with a checkable RegulonDB sign: 4072
- **Sign agreement (activates↔+, represses↔−): 100.0% (4072/4072)**

## What the gene→gene graph structurally cannot represent

- RegulonDB sign distribution: {'6)function': 1, '-': 3617, '+': 3370, '-+': 344, '?': 20}
- Unmappable regulators (sigma factors, sRNAs, small-molecule effectors like ppGpp, complexes): 14 distinct, covering 362 interactions.
  Top unmapped: ppgpp(308), rcsb-bglj(16), carbon storage regulator csra(14), hipab(5), dan(4), atp-dependent rna helicase dead(3), dinj-yafq(3), selb-l-selenocysteinyl-trna<sup>sec</sup>(2), small heat shock protein ibpa(2), 2)regulatorname(1), istr-1(1), ribonuclease e(1), threonine&mdash;trna ligase(1), h-+ns(1)

## Interpretation

- Recall is the ceiling on what perturbation effects the simulator can ever reproduce: any RegulonDB interaction absent from the graph is a response the simulator physically cannot make.
- Unmappable regulators expose the operator/sigma/sRNA structure gap: RegulonDB regulation routed through sigma factors, sRNAs and small-molecule effectors is collapsed or dropped, which is why true L3 (AND/OR operator logic) cannot yet be represented.
- Sign accuracy < 100% flags edges whose direction disagrees with the curated standard — data-quality items to fix before publication.
