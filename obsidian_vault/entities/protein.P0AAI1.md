---
entity_id: "protein.P0AAI1"
entity_type: "protein"
name: "ssuB"
source_database: "UniProt"
source_id: "P0AAI1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01724}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01724}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ssuB ycbE b0933 JW0916"
---

# ssuB

`protein.P0AAI1`

## Static

- Type: `protein`
- Source: `UniProt:P0AAI1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01724}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01724}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex SsuABC involved in aliphatic sulfonates import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:10506196, ECO:0000305|PubMed:10781534}. SsuB is the predicted ATP-binding component of an aliphatic sulfonate ABC transporter; SsuB contains sequence motifs conserved in ATP-binding cassette (ABC) proteins . A ΔssuBC strain is unable to grow using a range of aliphatic sulfonates as sulfur source including ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, sulfoacetate, 4-phenyl-1-butanesulfonate, N-phenyltaurine, MOPS and HEPES and growth is significantly reduced with propanesulfonate, pentanesulfonate, 2-(4-pyridyl)ethanesulfonate or PIPES as sulfur source. Wild type growth is restored when ssuB and ssuC are expressed from a plasmid .

## Biological Role

Component of aliphatic sulfonate ABC transporter (complex.ecocyc.ABC-56-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex SsuABC involved in aliphatic sulfonates import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:10506196, ECO:0000305|PubMed:10781534}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-56-CPLX|complex.ecocyc.ABC-56-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0933|gene.b0933]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAI1`
- `KEGG:ecj:JW0916;eco:b0933;ecoc:C3026_05730;`
- `GeneID:947220;`
- `GO:GO:0005524; GO:0010438; GO:0016020; GO:0016887; GO:0042918; GO:0042959; GO:0055052`
- `EC:7.6.2.14`

## Notes

Aliphatic sulfonates import ATP-binding protein SsuB (EC 7.6.2.14)
