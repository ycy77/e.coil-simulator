---
entity_id: "protein.P45475"
entity_type: "protein"
name: "ubiV"
source_database: "UniProt"
source_id: "P45475"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiV yhbV b3159 JW5530"
---

# ubiV

`protein.P45475`

## Static

- Type: `protein`
- Source: `UniProt:P45475`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the UbiUV hydroxylase, which is involved in the oxygen-independent ubiquinone (coenzyme Q) biosynthesis (PubMed:31289180, PubMed:37283518, PubMed:38507448). It catalyzes the three hydroxylation steps, using prephenate as the oxygen donor (PubMed:38507448). UbiUV ensures the production of ubiquinone under a range of O(2) levels, from anaerobiosis to microaerobiosis (PubMed:37283518). The UbiUV-dependent ubiquinone biosynthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis (PubMed:37283518). When produced at sufficiently high level, UbiUV can also hydroxylate ubiquinone precursors under aerobic conditions (PubMed:37283518). It contributes, though modestly, to bacterial multiplication in the mouse gut (PubMed:37283518). {ECO:0000269|PubMed:31289180, ECO:0000269|PubMed:37283518, ECO:0000269|PubMed:38507448}. UbiV together with UbiU functions in the three hydroxylation reactions in the oxygen-independent pathway for ubiquinone biosynthesis . UbiV contains a 4Fe-4S iron-sulfur cluster; mutagenesis of the cysteine residues C39, C180, C193, and C197 identified them as the iron-chelating residues. UbiU and UbiV can be purified as a heterodimer . A ΔubiV mutant is deficient in ubiquinone-8 biosynthesis under anaerobic growth conditions . UbiV: "ubiquinone biosynthesis V"

## Biological Role

Component of 2-(all-trans-polyprenyl)phenol 6-hydroxylase (prephenate) (complex.ecocyc.CPLX0-8308).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Component of the UbiUV hydroxylase, which is involved in the oxygen-independent ubiquinone (coenzyme Q) biosynthesis (PubMed:31289180, PubMed:37283518, PubMed:38507448). It catalyzes the three hydroxylation steps, using prephenate as the oxygen donor (PubMed:38507448). UbiUV ensures the production of ubiquinone under a range of O(2) levels, from anaerobiosis to microaerobiosis (PubMed:37283518). The UbiUV-dependent ubiquinone biosynthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis (PubMed:37283518). When produced at sufficiently high level, UbiUV can also hydroxylate ubiquinone precursors under aerobic conditions (PubMed:37283518). It contributes, though modestly, to bacterial multiplication in the mouse gut (PubMed:37283518). {ECO:0000269|PubMed:31289180, ECO:0000269|PubMed:37283518, ECO:0000269|PubMed:38507448}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8308|complex.ecocyc.CPLX0-8308]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3159|gene.b3159]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45475`
- `KEGG:ecj:JW5530;eco:b3159;ecoc:C3026_17205;`
- `GeneID:949117;`
- `GO:GO:0006744; GO:0046872; GO:0051539`
- `EC:1.97.1.15`

## Notes

Ubiquinone biosynthesis hydroxylase UbiV (EC 1.97.1.15) (2-(all-trans-polyprenyl)phenol 6-hydroxylase subunit UbiV)
