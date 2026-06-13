---
entity_id: "protein.P0AGI4"
entity_type: "protein"
name: "xylH"
source_database: "UniProt"
source_id: "P0AGI4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylH b3568 JW3540"
---

# xylH

`protein.P0AGI4`

## Static

- Type: `protein`
- Source: `UniProt:P0AGI4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for D-xylose. Probably responsible for the translocation of the substrate across the membrane. XylH is the predicted integral membrane subunit of a high-affinity, ATP dependent xylose uptake system .

## Biological Role

Component of xylose ABC transporter (complex.ecocyc.ABC-33-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for D-xylose. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-33-CPLX|complex.ecocyc.ABC-33-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3568|gene.b3568]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGI4`
- `KEGG:ecj:JW3540;eco:b3568;ecoc:C3026_19345;`
- `GeneID:948083;`
- `GO:GO:0005886; GO:0015752; GO:0015753; GO:0016020; GO:0022857; GO:0042732; GO:0055052`

## Notes

Xylose transport system permease protein XylH
