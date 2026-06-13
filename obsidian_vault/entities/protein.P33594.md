---
entity_id: "protein.P33594"
entity_type: "protein"
name: "nikE"
source_database: "UniProt"
source_id: "P33594"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01712}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01712}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nikE b3480 JW3445"
---

# nikE

`protein.P33594`

## Static

- Type: `protein`
- Source: `UniProt:P33594`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01712}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01712}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex NikABCDE involved in nickel import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01712}. NikE is one of two predicted ATP-binding subunits of a high affinity uptake system for Ni2+; NikE contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Component of Ni(2+) ABC transporter (complex.ecocyc.ABC-20-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex NikABCDE involved in nickel import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01712}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-20-CPLX|complex.ecocyc.ABC-20-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3480|gene.b3480]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33594`
- `KEGG:ecj:JW3445;eco:b3480;ecoc:C3026_18845;`
- `GeneID:947987;`
- `GO:GO:0005524; GO:0005886; GO:0006974; GO:0015413; GO:0015640; GO:0016020; GO:0016151; GO:0016887; GO:0055052; GO:0098716`
- `EC:7.2.2.11`

## Notes

Nickel import ATP-binding protein NikE (EC 7.2.2.11)
