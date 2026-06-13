---
entity_id: "protein.P75796"
entity_type: "protein"
name: "gsiA"
source_database: "UniProt"
source_id: "P75796"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gsiA yliA b0829 JW5897"
---

# gsiA

`protein.P75796`

## Static

- Type: `protein`
- Source: `UniProt:P75796`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:16109926}. GsiA is the predicted ATP binding subunit of a glutathione ABC importer; GsiA contains an ABC-ABC domain

## Biological Role

Component of glutathione ABC transporter (complex.ecocyc.ABC-49-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex GsiABCD involved in glutathione import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:16109926}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0829|gene.b0829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75796`
- `KEGG:ecj:JW5897;eco:b0829;ecoc:C3026_05200;`
- `GeneID:945457;`
- `GO:GO:0005524; GO:0005886; GO:0016020; GO:0016887; GO:0034634; GO:0034775; GO:0042626; GO:0055052`
- `EC:7.4.2.10`

## Notes

Glutathione import ATP-binding protein GsiA (EC 7.4.2.10)
