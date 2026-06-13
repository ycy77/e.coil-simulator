---
entity_id: "protein.P37744"
entity_type: "protein"
name: "rfbA"
source_database: "UniProt"
source_id: "P37744"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rfbA rmlA rmlA1 b2039 JW2024"
---

# rfbA

`protein.P37744`

## Static

- Type: `protein`
- Source: `UniProt:P37744`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate, as well as its pyrophosphorolysis. {ECO:0000269|PubMed:11697907}.

## Biological Role

Catalyzes dTTP:alpha-D-glucose-1-phosphate thymidylyltransferase (reaction.R02328). Component of glucose-1-phosphate thymidylyltransferase 1 (complex.ecocyc.CPLX0-8034).

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

FUNCTION: Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate, as well as its pyrophosphorolysis. {ECO:0000269|PubMed:11697907}.

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
- `is_component_of` --> [[complex.ecocyc.CPLX0-8034|complex.ecocyc.CPLX0-8034]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2039|gene.b2039]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37744`
- `KEGG:ecj:JW2024;eco:b2039;ecoc:C3026_11485;`
- `GeneID:945154;`
- `GO:GO:0000271; GO:0005829; GO:0008879; GO:0009243; GO:0019305; GO:0042802; GO:0046872; GO:0051289`
- `EC:2.7.7.24`

## Notes

Glucose-1-phosphate thymidylyltransferase 1 (G1P-TT 1) (EC 2.7.7.24) (dTDP-glucose pyrophosphorylase 1) (dTDP-glucose synthase 1)
