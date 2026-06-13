---
entity_id: "protein.P0AGH8"
entity_type: "protein"
name: "pstC"
source_database: "UniProt"
source_id: "P0AGH8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pstC phoW b3727 JW3705"
---

# pstC

`protein.P0AGH8`

## Static

- Type: `protein`
- Source: `UniProt:P0AGH8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for phosphate; probably responsible for the translocation of the substrate across the membrane. PstC is one of two inner membrane subunits of an ATP-dependent high affinity phosphate uptake system. pstC belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Component of phosphate ABC transporter (complex.ecocyc.ABC-27-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for phosphate; probably responsible for the translocation of the substrate across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-27-CPLX|complex.ecocyc.ABC-27-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3727|gene.b3727]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGH8`
- `KEGG:ecj:JW3705;eco:b3727;ecoc:C3026_20200;`
- `GeneID:86948631;93778214;948238;`
- `GO:GO:0005315; GO:0005886; GO:0009314; GO:0016020; GO:0035435; GO:0055052`

## Notes

Phosphate transport system permease protein PstC
