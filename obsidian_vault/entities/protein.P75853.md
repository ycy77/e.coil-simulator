---
entity_id: "protein.P75853"
entity_type: "protein"
name: "ssuA"
source_database: "UniProt"
source_id: "P75853"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ssuA ycbO b0936 JW0919"
---

# ssuA

`protein.P75853`

## Static

- Type: `protein`
- Source: `UniProt:P75853`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of a binding-protein-dependent transport system for aliphatic sulfonates. Putative binding protein. SsuA is the predicted substrate-binding protein of an ATP-dependent aliphatic sulfonate uptake system . A ΔssuA strain is unable to grow using a range of aliphatic sulfonates as sulfur source including ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, sulfoacetate, N-phenyltaurine, 4-phenyl-1-butansulfonate, MOPS and HEPES and has significantly reduced growth with propanesulfonate, pentanesulfonate, 2-(4-pyridyl)ethanesulfonate or PIPES as sulfur source. Wild type growth is restored when ssuA is expressed from a plasmid .

## Biological Role

Component of aliphatic sulfonate ABC transporter (complex.ecocyc.ABC-56-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of a binding-protein-dependent transport system for aliphatic sulfonates. Putative binding protein.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-56-CPLX|complex.ecocyc.ABC-56-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0936|gene.b0936]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75853`
- `KEGG:ecj:JW0919;eco:b0936;ecoc:C3026_05745;`
- `GeneID:945560;`
- `GO:GO:0006790; GO:0010438; GO:0016020; GO:0042597; GO:0042918; GO:0042959; GO:0055052`

## Notes

Putative aliphatic sulfonates-binding protein
