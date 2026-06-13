---
entity_id: "protein.P06611"
entity_type: "protein"
name: "btuD"
source_database: "UniProt"
source_id: "P06611"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btuD b1709 JW1699"
---

# btuD

`protein.P06611`

## Static

- Type: `protein`
- Source: `UniProt:P06611`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01005}. BtuD is the ATP-binding component of a high-affinity vitamin B12 uptake system; BtuB contains sequence motifs that are conserved in ATP binding cassette (ABC) proteins A Tn10 insertion in the btuCED promoter region restores colony-forming ability to an rne mutant. The suppression phenotype is reversed by overexpression of btuC, E or D .

## Biological Role

Component of vitamin B12 ABC transporter (complex.ecocyc.ABC-5-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01005}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-5-CPLX|complex.ecocyc.ABC-5-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1709|gene.b1709]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06611`
- `KEGG:ecj:JW1699;eco:b1709;ecoc:C3026_09785;`
- `GeneID:945751;`
- `GO:GO:0005524; GO:0015420; GO:0015889; GO:0016020; GO:0016887; GO:0019898; GO:0042626; GO:0043190; GO:1990191; GO:1990193`
- `EC:7.6.2.8`

## Notes

Vitamin B12 import ATP-binding protein BtuD (EC 7.6.2.8) (Vitamin B12-transporting ATPase)
