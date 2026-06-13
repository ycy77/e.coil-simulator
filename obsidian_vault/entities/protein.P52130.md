---
entity_id: "protein.P52130"
entity_type: "protein"
name: "rnlB"
source_database: "UniProt"
source_id: "P52130"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnlB yfjO b2631 JW5418"
---

# rnlB

`protein.P52130`

## Static

- Type: `protein`
- Source: `UniProt:P52130`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. A labile antitoxin (half-life of 2.1 minutes) that inhibits the endonuclease activity of cognate toxin RnlA but not that of non-cognate toxin LsoA. {ECO:0000269|PubMed:20980243, ECO:0000269|PubMed:22403819}. RnlB is the antitoxin of the RnlA-RnlB toxin-antitoxin system. Overexpression of RnlA in ΔrnlAB cells inhibits cell growth and causes mRNA degradation, while overexpression of RnlB in wild-type cells suppresses the growth defect of the T4 dmd mutant . The RnlB protein is extremely unstable and is stabilized in clpX or lon mutants . RnlB interacts with the DBD domain of RnlA and suppresses its RNase LS activity . Reviews: , Comments:

## Biological Role

Component of RnlA-RnlB toxin-antitoxin complex (complex.ecocyc.CPLX0-7909).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. A labile antitoxin (half-life of 2.1 minutes) that inhibits the endonuclease activity of cognate toxin RnlA but not that of non-cognate toxin LsoA. {ECO:0000269|PubMed:20980243, ECO:0000269|PubMed:22403819}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7909|complex.ecocyc.CPLX0-7909]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2631|gene.b2631]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52130`
- `KEGG:ecj:JW5418;eco:b2631;ecoc:C3026_14555;`
- `GeneID:947113;`
- `GO:GO:0006355; GO:0040008; GO:0044010; GO:0110001`

## Notes

Antitoxin RnlB
