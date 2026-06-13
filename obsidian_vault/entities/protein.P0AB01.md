---
entity_id: "protein.P0AB01"
entity_type: "protein"
name: "elyC"
source_database: "UniProt"
source_id: "P0AB01"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "elyC ycbC b0920 JW0903"
---

# elyC

`protein.P0AB01`

## Static

- Type: `protein`
- Source: `UniProt:P0AB01`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Plays a critical role in the metabolism of the essential lipid carrier used for cell wall synthesis. {ECO:0000269|PubMed:24391520}. Cells lacking ElyC have a defect in peptidoglycan synthesis and genetic analysis suggests a role for ElyC in CPD-9646 metabolism . ΔelyC cells show an excess of protein aggregation; overproduction of the periplasmic chaperones, Spy or DsbG, reduces this to a wild-type level . ElyC and CPD0-2646 (ECACYC) are implicated in a pathway that regulates synthesis of CPD-21605 "phosphoglyceride-linked ECA" (ECAPG); ElyC inhibits production of ECAPG most likely at a posttranscriptional level; the full function of ElyC requires ECACYC (consider also ). A ΔelyC mutant grows poorly and forms small colonies at room temperature. In a screen developed to identify genes associated with envelope biogenesis disorders, a ΔelyC mutant has a positive phenotype (chlorophenyl red-β-D-galactopyranoside+ or CPRG+). The growth defect and CPRG+ phenotype can be complemented by expressing elyC in trans. Overproduction of UPPSYN-CPLX "UppS" also specifically suppresses the phenotype associated with loss of ElyC function. ΔelyCΔmrcB cells are not viable at room temperature . ElyC contains two predicted trans-membrane regions plus a large domain of unknown function (DUF218) that is probably located in the periplasm . elyC: elevated frequency of lysis C

## Annotation

FUNCTION: Plays a critical role in the metabolism of the essential lipid carrier used for cell wall synthesis. {ECO:0000269|PubMed:24391520}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0920|gene.b0920]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB01`
- `KEGG:ecj:JW0903;eco:b0920;ecoc:C3026_05660;`
- `GeneID:945546;`
- `GO:GO:0000270; GO:0005886; GO:0006457; GO:0043164; GO:0071555`

## Notes

Envelope biogenesis factor ElyC (Elevated frequency of lysis)
