---
entity_id: "protein.P0AAH0"
entity_type: "protein"
name: "pstB"
source_database: "UniProt"
source_id: "P0AAH0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pstB phoT b3725 JW3703"
---

# pstB

`protein.P0AAH0`

## Static

- Type: `protein`
- Source: `UniProt:P0AAH0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex PstSACB involved in phosphate import. Responsible for energy coupling to the transport system. PstB is the ATP-binding subunit of a high affinity phosphate specific uptake system; PstB contains signature motifs conserved in ATP binding cassette (ABC) proteins . PstB interacts directly with PhoU and this interaction is implicated in signal transduction to PhoR; PstB, PhoU and PhoR may form a phosphate-sensing complex at the cell membrane . pstB belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Component of phosphate ABC transporter (complex.ecocyc.ABC-27-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex PstSACB involved in phosphate import. Responsible for energy coupling to the transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-27-CPLX|complex.ecocyc.ABC-27-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3725|gene.b3725]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAH0`
- `KEGG:ecj:JW3703;eco:b3725;ecoc:C3026_20190;`
- `GeneID:93778212;948240;`
- `GO:GO:0005315; GO:0005524; GO:0005886; GO:0006817; GO:0015415; GO:0016020; GO:0016887; GO:0035435; GO:0055052`
- `EC:7.3.2.1`

## Notes

Phosphate import ATP-binding protein PstB (EC 7.3.2.1) (ABC phosphate transporter) (Phosphate-transporting ATPase)
