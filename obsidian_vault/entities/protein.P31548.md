---
entity_id: "protein.P31548"
entity_type: "protein"
name: "thiQ"
source_database: "UniProt"
source_id: "P31548"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01723}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01723}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiQ yabJ b0066 JW0065"
---

# thiQ

`protein.P31548`

## Static

- Type: `protein`
- Source: `UniProt:P31548`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01723}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01723}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:12175925, ECO:0000305}. ThiQ is the predicted ATP-binding subunit of a thiamine uptake system; ThiQ contains sequence motifs conserved in ATP-binding cassette (ABC) proteins

## Biological Role

Component of thiamine ABC transporter (complex.ecocyc.ABC-32-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:12175925, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-32-CPLX|complex.ecocyc.ABC-32-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0066|gene.b0066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31548`
- `KEGG:ecj:JW0065;eco:b0066;`
- `GeneID:944785;`
- `GO:GO:0005524; GO:0005886; GO:0015234; GO:0016020; GO:0016887; GO:0048502; GO:0055052; GO:0071934; GO:0140359`
- `EC:7.6.2.15`

## Notes

Thiamine import ATP-binding protein ThiQ (EC 7.6.2.15)
