---
entity_id: "protein.P77257"
entity_type: "protein"
name: "lsrA"
source_database: "UniProt"
source_id: "P77257"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrA ego ydeX b1513 JW1506"
---

# lsrA

`protein.P77257`

## Static

- Type: `protein`
- Source: `UniProt:P77257`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Responsible for energy coupling to the transport system. {ECO:0000305|PubMed:15601708}. Based on sequence similarity lsrA is predicted to encode the ATP-binding component of an AI-2 ABC transporter . lsrA is required for growth under optimum growth conditions (rich medium at 37°C), but not under cold conditions (15°C) or in minimal medium .

## Biological Role

Component of Autoinducer-2 ABC transporter (complex.ecocyc.ABC-58-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LsrABCD involved in autoinducer 2 (AI-2) import. Responsible for energy coupling to the transport system. {ECO:0000305|PubMed:15601708}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-58-CPLX|complex.ecocyc.ABC-58-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1513|gene.b1513]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77257`
- `KEGG:ecj:JW1506;eco:b1513;ecoc:C3026_08750;`
- `GeneID:945680;`
- `GO:GO:0005524; GO:0005886; GO:0009372; GO:0016020; GO:0016887; GO:0022857; GO:0055052; GO:1905887`
- `EC:7.6.2.13`

## Notes

Autoinducer 2 import ATP-binding protein LsrA (AI-2 import ATP-binding protein LsrA) (EC 7.6.2.13) (EGO10A)
