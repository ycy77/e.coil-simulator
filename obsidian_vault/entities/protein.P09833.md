---
entity_id: "protein.P09833"
entity_type: "protein"
name: "modC"
source_database: "UniProt"
source_id: "P09833"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "modC chlD narD b0765 JW0748"
---

# modC

`protein.P09833`

## Static

- Type: `protein`
- Source: `UniProt:P09833`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ModABC involved in molybdenum import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01705}. ModC is the predicted ATP-binding component of of an ABC transporter that mediates the high affinity uptake of molybdate. ModC contains an ABC-ABC domain .

## Biological Role

Component of molybdate ABC transporter (complex.ecocyc.ABC-19-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ModABC involved in molybdenum import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01705}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-19-CPLX|complex.ecocyc.ABC-19-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0765|gene.b0765]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09833`
- `KEGG:ecj:JW0748;eco:b0765;ecoc:C3026_03880;`
- `GeneID:93776716;945362;`
- `GO:GO:0005524; GO:0015098; GO:0015412; GO:0015689; GO:0016020; GO:0016887; GO:0055052; GO:0070614`
- `EC:7.3.2.5`

## Notes

Molybdenum import ATP-binding protein ModC (EC 7.3.2.5)
