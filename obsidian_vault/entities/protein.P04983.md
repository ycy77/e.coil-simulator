---
entity_id: "protein.P04983"
entity_type: "protein"
name: "rbsA"
source_database: "UniProt"
source_id: "P04983"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000305|PubMed:25533465}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000305|PubMed:25533465}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbsA b3749 JW3728"
---

# rbsA

`protein.P04983`

## Static

- Type: `protein`
- Source: `UniProt:P04983`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000305|PubMed:25533465}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000305|PubMed:25533465}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:6327617, ECO:0000269|PubMed:8762140}. RbsA is the ATP-binding subunit of a high affinity ribose uptake system; RbsA contains a signature motifs conserved in ATP-binding cassette (ABC) proteins; RbsA contains an ABC-ABC domain

## Biological Role

Component of ribose ABC transporter (complex.ecocyc.ABC-28-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01716, ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:6327617, ECO:0000269|PubMed:8762140}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-28-CPLX|complex.ecocyc.ABC-28-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3749|gene.b3749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04983`
- `KEGG:ecj:JW3728;eco:b3749;ecoc:C3026_20310;`
- `GeneID:75173983;948264;`
- `GO:GO:0005524; GO:0005886; GO:0015147; GO:0015407; GO:0015591; GO:0015611; GO:0015752; GO:0016020; GO:0016887; GO:0043190; GO:0055052`
- `EC:7.5.2.7`

## Notes

Ribose import ATP-binding protein RbsA (EC 7.5.2.7)
