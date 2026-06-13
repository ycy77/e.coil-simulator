---
entity_id: "protein.P37747"
entity_type: "protein"
name: "glf"
source_database: "UniProt"
source_id: "P37747"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glf yefE b2036 JW2021"
---

# glf

`protein.P37747`

## Static

- Type: `protein`
- Source: `UniProt:P37747`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion through a 2-keto intermediate of uridine diphosphogalactopyranose (UDP-GalP) into uridine diphosphogalactofuranose (UDP-GalF). {ECO:0000250, ECO:0000269|PubMed:11448178, ECO:0000269|PubMed:8576037}.

## Biological Role

Catalyzes UDP-alpha-D-galactopyranose furanomutase (reaction.R00505), UDP-L-arabinopyranose furanomutase (reaction.R09009). Component of UDP-galactopyranose mutase (complex.ecocyc.CPLX0-8582).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion through a 2-keto intermediate of uridine diphosphogalactopyranose (UDP-GalP) into uridine diphosphogalactofuranose (UDP-GalF). {ECO:0000250, ECO:0000269|PubMed:11448178, ECO:0000269|PubMed:8576037}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00505|reaction.R00505]] `KEGG` `database` - via EC:5.4.99.9
- `catalyzes` --> [[reaction.R09009|reaction.R09009]] `KEGG` `database` - via EC:5.4.99.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-8582|complex.ecocyc.CPLX0-8582]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2036|gene.b2036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37747`
- `KEGG:ecj:JW2021;eco:b2036;ecoc:C3026_11470;`
- `GeneID:945235;`
- `GO:GO:0005829; GO:0008767; GO:0009103; GO:0042803; GO:0050660`
- `EC:5.4.99.9`

## Notes

UDP-galactopyranose mutase (UGM) (EC 5.4.99.9) (UDP-GALP mutase) (Uridine 5-diphosphate galactopyranose mutase)
