---
entity_id: "protein.P37649"
entity_type: "protein"
name: "pdeK"
source_database: "UniProt"
source_id: "P37649"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeK yhjK b3529 JW5943"
---

# pdeK

`protein.P37649`

## Static

- Type: `protein`
- Source: `UniProt:P37649`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}.

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991). Component of cyclic di-GMP phosphodiesterase PdeK (complex.ecocyc.CPLX0-8555).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52
- `is_component_of` --> [[complex.ecocyc.CPLX0-8555|complex.ecocyc.CPLX0-8555]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3529|gene.b3529]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37649`
- `KEGG:ecj:JW5943;eco:b3529;`
- `GeneID:948048;`
- `GO:GO:0005886; GO:0007165; GO:0042802; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeK (EC 3.1.4.52)
