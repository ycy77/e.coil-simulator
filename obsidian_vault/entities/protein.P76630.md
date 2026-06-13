---
entity_id: "protein.P76630"
entity_type: "protein"
name: "ygaZ"
source_database: "UniProt"
source_id: "P76630"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygaZ b2682 JW2657"
---

# ygaZ

`protein.P76630`

## Static

- Type: `protein`
- Source: `UniProt:P76630`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

Inner membrane protein YgaZ YgaZ is one protein of a putative two-component transporter that is implicated in L-valine export in E. coli K-12. YgaZ has 27% identity to the BrnF protein of the Corynebacterium glutamicum methionine/branched chain amino acid export system . The expression of ygaZ is significantly induced when cells are cultured on mouse cecal mucus compared to cells grown on glucose .

## Biological Role

Component of L-valine exporter (complex.ecocyc.CPLX0-7684).

## Annotation

Inner membrane protein YgaZ

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7684|complex.ecocyc.CPLX0-7684]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2682|gene.b2682]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76630`
- `KEGG:ecj:JW2657;eco:b2682;ecoc:C3026_14770;`
- `GeneID:945093;`
- `GO:GO:0005886; GO:1902495; GO:1903785`

## Notes

Inner membrane protein YgaZ
