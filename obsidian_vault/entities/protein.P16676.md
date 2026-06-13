---
entity_id: "protein.P16676"
entity_type: "protein"
name: "cysA"
source_database: "UniProt"
source_id: "P16676"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01701}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01701}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysA b2422 JW2415"
---

# cysA

`protein.P16676`

## Static

- Type: `protein`
- Source: `UniProt:P16676`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01701}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01701}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CysAWTP involved in sulfate/thiosulfate import. Responsible for energy coupling to the transport system. cysA encodes the predicted ATP-binding subunit of a high-affinity sulfate/thiosulfate uptake system; CysA contains sequence motifs conserved in ATP-binding cassette (ABC) proteins .

## Biological Role

Component of thiosulfate/sulfate ABC transporter (complex.ecocyc.ABC-7-CPLX), sulfate/thiosulfate ABC transporter (complex.ecocyc.ABC-70-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CysAWTP involved in sulfate/thiosulfate import. Responsible for energy coupling to the transport system.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2422|gene.b2422]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16676`
- `KEGG:ecj:JW2415;eco:b2422;ecoc:C3026_13460;`
- `GeneID:75172536;946889;`
- `GO:GO:0005524; GO:0015419; GO:0015709; GO:0016020; GO:0016887; GO:0035796; GO:0102025; GO:1902358`
- `EC:7.3.2.3`

## Notes

Sulfate/thiosulfate import ATP-binding protein CysA (EC 7.3.2.3) (Sulfate-transporting ATPase)
