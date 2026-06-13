---
entity_id: "protein.P0ABH7"
entity_type: "protein"
name: "gltA"
source_database: "UniProt"
source_id: "P0ABH7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltA gluT icdB b0720 JW0710"
---

# gltA

`protein.P0ABH7`

## Static

- Type: `protein`
- Source: `UniProt:P0ABH7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Citrate synthase (EC 2.3.3.16)

## Biological Role

Catalyzes acetyl-CoA:oxaloacetate C-acetyltransferase (thioester-hydrolysing) (reaction.R00351). Component of citrate synthase (complex.ecocyc.CITRATE-SI-SYNTHASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Citrate synthase (EC 2.3.3.16)

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00351|reaction.R00351]] `KEGG` `database` - via EC:2.3.3.1
- `is_component_of` --> [[complex.ecocyc.CITRATE-SI-SYNTHASE|complex.ecocyc.CITRATE-SI-SYNTHASE]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0720|gene.b0720]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABH7`
- `KEGG:ecj:JW0710;eco:b0720;ecoc:C3026_03600;`
- `GeneID:93776765;945323;`
- `GO:GO:0005829; GO:0006099; GO:0034214; GO:0036440; GO:0042802; GO:0070404`
- `EC:2.3.3.16`

## Notes

Citrate synthase (EC 2.3.3.16)
