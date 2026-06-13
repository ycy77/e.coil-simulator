---
entity_id: "protein.P13518"
entity_type: "protein"
name: "csrD"
source_database: "UniProt"
source_id: "P13518"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csrD yhdA b3252 JW3221"
---

# csrD

`protein.P13518`

## Static

- Type: `protein`
- Source: `UniProt:P13518`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Serves as a specificity factor required for RNase E-mediated decay of the small global regulatory RNAs CsrB and CsrC, it is probably not a nuclease. Nor does its activity involve c-di-GMP, despite its domain composition. Positively modulates motility gene expression, is also required for curli expression. {ECO:0000269|PubMed:16980588, ECO:0000269|PubMed:17064377, ECO:0000269|PubMed:19332833}.

## Biological Role

Component of regulator of CsrB and CsrC decay (complex.ecocyc.CPLX0-8245).

## Annotation

FUNCTION: Serves as a specificity factor required for RNase E-mediated decay of the small global regulatory RNAs CsrB and CsrC, it is probably not a nuclease. Nor does its activity involve c-di-GMP, despite its domain composition. Positively modulates motility gene expression, is also required for curli expression. {ECO:0000269|PubMed:16980588, ECO:0000269|PubMed:17064377, ECO:0000269|PubMed:19332833}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8245|complex.ecocyc.CPLX0-8245]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3252|gene.b3252]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13518`
- `KEGG:ecj:JW3221;eco:b3252;ecoc:C3026_17685;`
- `GeneID:947702;`
- `GO:GO:0005886; GO:0006401; GO:0032991; GO:0042802; GO:0051252; GO:0071111`

## Notes

RNase E specificity factor CsrD (Regulator of CsrB and CsrC decay CsrD)
