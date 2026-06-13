---
entity_id: "protein.P16677"
entity_type: "protein"
name: "phnC"
source_database: "UniProt"
source_id: "P16677"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01713}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01713}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnC b4106 JW4067"
---

# phnC

`protein.P16677`

## Static

- Type: `protein`
- Source: `UniProt:P16677`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01713}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01713}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PhnCDE involved in phosphonates, phosphate esters, phosphite and phosphate import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:1846145, ECO:0000269|PubMed:8388873}. phnC encodes the ATP binding subunit of a phosphonate/phosphate uptake system that is considered to be cryptic in E. coli K-12.phnC contains signature motifs conserved in ATP-binding cassette proteins .

## Biological Role

Component of phosphonate/phosphate ABC transporter (complex.ecocyc.ABC-23-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PhnCDE involved in phosphonates, phosphate esters, phosphite and phosphate import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:1846145, ECO:0000269|PubMed:8388873}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-23-CPLX|complex.ecocyc.ABC-23-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4106|gene.b4106]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16677`
- `KEGG:ecj:JW4067;eco:b4106;ecoc:C3026_22185;`
- `GeneID:948623;`
- `GO:GO:0005524; GO:0005886; GO:0015416; GO:0016887; GO:0042626`
- `EC:7.3.2.2`

## Notes

Phosphonates import ATP-binding protein PhnC (EC 7.3.2.2)
