---
entity_id: "protein.P61887"
entity_type: "protein"
name: "rffH"
source_database: "UniProt"
source_id: "P61887"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rffH rmlA2 yifG b3789 JW3763"
---

# rffH

`protein.P61887`

## Static

- Type: `protein`
- Source: `UniProt:P61887`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate, as well as its pyrophosphorolysis. {ECO:0000269|PubMed:7559340}.

## Biological Role

Catalyzes dTTP:alpha-D-glucose-1-phosphate thymidylyltransferase (reaction.R02328). Component of glucose-1-phosphate thymidylyltransferase 2 (complex.ecocyc.CPLX0-8012).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate, as well as its pyrophosphorolysis. {ECO:0000269|PubMed:7559340}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02328|reaction.R02328]] `KEGG` `database` - via EC:2.7.7.24
- `is_component_of` --> [[complex.ecocyc.CPLX0-8012|complex.ecocyc.CPLX0-8012]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3789|gene.b3789]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P61887`
- `KEGG:ecj:JW3763;eco:b3789;ecoc:C3026_20515;`
- `GeneID:75174021;948299;`
- `GO:GO:0000271; GO:0000287; GO:0005829; GO:0008879; GO:0009243; GO:0009246; GO:0042802`
- `EC:2.7.7.24`

## Notes

Glucose-1-phosphate thymidylyltransferase 2 (G1P-TT 2) (EC 2.7.7.24) (dTDP-glucose pyrophosphorylase 2) (dTDP-glucose synthase 2)
