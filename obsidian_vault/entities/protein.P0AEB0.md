---
entity_id: "protein.P0AEB0"
entity_type: "protein"
name: "cysW"
source_database: "UniProt"
source_id: "P0AEB0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysW b2423 JW2416"
---

# cysW

`protein.P0AEB0`

## Static

- Type: `protein`
- Source: `UniProt:P0AEB0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. Probably responsible for the translocation of the substrate across the membrane. CysW is one of two predicted inner membrane subunits of an ATP-dependent sulfate/thiosulfate uptake system; CysW contains 50% hydrophobic residues

## Biological Role

Component of thiosulfate/sulfate ABC transporter (complex.ecocyc.ABC-7-CPLX), sulfate/thiosulfate ABC transporter (complex.ecocyc.ABC-70-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex CysAWTP (TC 3.A.1.6.1) involved in sulfate/thiosulfate import. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2423|gene.b2423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEB0`
- `KEGG:ecj:JW2416;eco:b2423;ecoc:C3026_13465;`
- `GeneID:2847743;93774708;`
- `GO:GO:0005886; GO:0015419; GO:0015709; GO:0016020; GO:0035796; GO:1902358`

## Notes

Sulfate transport system permease protein CysW
