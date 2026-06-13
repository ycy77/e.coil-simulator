---
entity_id: "protein.P33593"
entity_type: "protein"
name: "nikD"
source_database: "UniProt"
source_id: "P33593"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01711}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01711}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nikD b3479 JW3444"
---

# nikD

`protein.P33593`

## Static

- Type: `protein`
- Source: `UniProt:P33593`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01711}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01711}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex NikABCDE involved in nickel import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01711}. NikD is one of two predicted ATP-binding subunits of a high affinity uptake system for Ni2+; NikD contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Component of Ni(2+) ABC transporter (complex.ecocyc.ABC-20-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex NikABCDE involved in nickel import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01711}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-20-CPLX|complex.ecocyc.ABC-20-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3479|gene.b3479]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33593`
- `KEGG:ecj:JW3444;eco:b3479;ecoc:C3026_18840;`
- `GeneID:947989;`
- `GO:GO:0005524; GO:0005886; GO:0015413; GO:0016020; GO:0016151; GO:0016887; GO:0022857; GO:0035672; GO:0055052; GO:0098716`
- `EC:7.2.2.11`

## Notes

Nickel import ATP-binding protein NikD (EC 7.2.2.11)
