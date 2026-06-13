---
entity_id: "protein.P75851"
entity_type: "protein"
name: "ssuC"
source_database: "UniProt"
source_id: "P75851"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ssuC ycbM b0934 JW5121"
---

# ssuC

`protein.P75851`

## Static

- Type: `protein`
- Source: `UniProt:P75851`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of a binding-protein-dependent transport system for aliphatic sulfonates. Probably responsible for the translocation of the substrate across the membrane. SsuC is the predicted integral membrane component of an ATP-dependent aliphatic sulfonate uptake system . A ΔssuBC strain is unable to grow using a range of aliphatic sulfonates as sulfur source including ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, sulfoacetate, 4-phenyl-1-butanesulfonate, N-phenyltaurine, MOPS and HEPES and growth is significantly reduced with propanesulfonate, pentanesulfonate, 2-(4-pyridyl)ethanesulfonate or PIPES as sulfur source. Wild type growth is restored when ssuB and ssuC are expressed from a plasmid . SsuC is predicted to be an inner membrane protein with 6-7 transmembrane domains; topology analysis suggests the N and C termini are located in the cytoplasm .

## Biological Role

Component of aliphatic sulfonate ABC transporter (complex.ecocyc.ABC-56-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a binding-protein-dependent transport system for aliphatic sulfonates. Probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-56-CPLX|complex.ecocyc.ABC-56-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0934|gene.b0934]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75851`
- `KEGG:ecj:JW5121;eco:b0934;ecoc:C3026_05735;`
- `GeneID:93776480;947216;`
- `GO:GO:0005886; GO:0006790; GO:0010438; GO:0016020; GO:0042918; GO:0042959; GO:0055052`

## Notes

Putative aliphatic sulfonates transport permease protein SsuC
