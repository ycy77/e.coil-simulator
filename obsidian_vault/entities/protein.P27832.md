---
entity_id: "protein.P27832"
entity_type: "protein"
name: "wecD"
source_database: "UniProt"
source_id: "P27832"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecD rffC yifH b3790 JW5597"
---

# wecD

`protein.P27832`

## Static

- Type: `protein`
- Source: `UniProt:P27832`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the acetylation of dTDP-fucosamine (dTDP-4-amino-4,6-dideoxy-D-galactose) to dTDP-Fuc4NAc, which is utilized in the biosynthesis of the enterobacterial common antigen (ECA). {ECO:0000255|HAMAP-Rule:MF_02027}.

## Biological Role

Component of dTDP-4-amino-4,6-dideoxy-D-galactose acyltransferase (complex.ecocyc.CPLX0-8614).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the acetylation of dTDP-fucosamine (dTDP-4-amino-4,6-dideoxy-D-galactose) to dTDP-Fuc4NAc, which is utilized in the biosynthesis of the enterobacterial common antigen (ECA). {ECO:0000255|HAMAP-Rule:MF_02027}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8614|complex.ecocyc.CPLX0-8614]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3790|gene.b3790]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27832`
- `KEGG:ecj:JW5597;eco:b3790;ecoc:C3026_20520;`
- `GeneID:948298;`
- `GO:GO:0008080; GO:0009246`
- `EC:2.3.1.210`

## Notes

dTDP-fucosamine acetyltransferase (EC 2.3.1.210) (TDP-fucosamine acetyltransferase) (dTDP-4-amino-4,6-dideoxy-D-galactose acyltransferase)
