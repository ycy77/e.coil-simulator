---
entity_id: "protein.P08660"
entity_type: "protein"
name: "lysC"
source_database: "UniProt"
source_id: "P08660"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lysC apk b4024 JW3984"
---

# lysC

`protein.P08660`

## Static

- Type: `protein`
- Source: `UniProt:P08660`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Lysine-sensitive aspartokinase 3 (EC 2.7.2.4) (Aspartate kinase III) (AKIII) (Lysine-sensitive aspartokinase III)

## Biological Role

Catalyzes ATP:L-aspartate 4-phosphotransferase (reaction.R00480). Component of aspartate kinase III (complex.ecocyc.ASPKINIII-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Lysine-sensitive aspartokinase 3 (EC 2.7.2.4) (Aspartate kinase III) (AKIII) (Lysine-sensitive aspartokinase III)

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00480|reaction.R00480]] `KEGG` `database` - via EC:2.7.2.4
- `is_component_of` --> [[complex.ecocyc.ASPKINIII-CPLX|complex.ecocyc.ASPKINIII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4024|gene.b4024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08660`
- `KEGG:ecj:JW3984;eco:b4024;ecoc:C3026_21735;`
- `GeneID:948531;`
- `GO:GO:0004072; GO:0005524; GO:0005829; GO:0009089; GO:0009090; GO:0042803`
- `EC:2.7.2.4`

## Notes

Lysine-sensitive aspartokinase 3 (EC 2.7.2.4) (Aspartate kinase III) (AKIII) (Lysine-sensitive aspartokinase III)
