---
entity_id: "protein.P06609"
entity_type: "protein"
name: "btuC"
source_database: "UniProt"
source_id: "P06609"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btuC b1711 JW1701"
---

# btuC

`protein.P06609`

## Static

- Type: `protein`
- Source: `UniProt:P06609`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Involved in the translocation of the substrate across the membrane. BtuC is the integral membrane component an ATP-dependent vitamin B12 uptake system. A Tn10 insertion in the btuCED promoter region restores colony-forming ability to an rne mutant. The suppression phenotype is reversed by overexpression of btuC, E or D .

## Biological Role

Component of vitamin B12 ABC transporter (complex.ecocyc.ABC-5-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Involved in the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-5-CPLX|complex.ecocyc.ABC-5-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1711|gene.b1711]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06609`
- `KEGG:ecj:JW1701;eco:b1711;ecoc:C3026_09795;`
- `GeneID:945877;`
- `GO:GO:0005886; GO:0015420; GO:0015889; GO:0016020; GO:0022857; GO:0042802; GO:0043190; GO:1990191; GO:1990193`

## Notes

Vitamin B12 import system permease protein BtuC
