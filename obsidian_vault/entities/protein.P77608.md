---
entity_id: "protein.P77608"
entity_type: "protein"
name: "mhpD"
source_database: "UniProt"
source_id: "P77608"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpD b0350 JW0341"
---

# mhpD

`protein.P77608`

## Static

- Type: `protein`
- Source: `UniProt:P77608`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of 2-hydroxypentadienoic acid (enolic form of 2-oxopent-4-enoate) to 4-hydroxy-2-ketopentanoic acid. {ECO:0000269|PubMed:9492273}.

## Biological Role

Catalyzes 4-hydroxy-2-oxopentanoate hydro-lyase (2-oxopent-4-enoate-forming) (reaction.R02601), R05297 (reaction.R05297). Component of 2-hydroxypentadienoate hydratase (complex.ecocyc.CPLX0-7951).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of 2-hydroxypentadienoic acid (enolic form of 2-oxopent-4-enoate) to 4-hydroxy-2-ketopentanoic acid. {ECO:0000269|PubMed:9492273}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02601|reaction.R02601]] `KEGG` `database` - via EC:4.2.1.80
- `catalyzes` --> [[reaction.R05297|reaction.R05297]] `KEGG` `database` - via EC:4.2.1.80
- `is_component_of` --> [[complex.ecocyc.CPLX0-7951|complex.ecocyc.CPLX0-7951]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5

## Incoming Edges (1)

- `encodes` <-- [[gene.b0350|gene.b0350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77608`
- `KEGG:ecj:JW0341;eco:b0350;ecoc:C3026_24885;`
- `GeneID:944768;`
- `GO:GO:0005737; GO:0008684; GO:0019380; GO:0030145; GO:0042802`
- `EC:4.2.1.80`

## Notes

2-keto-4-pentenoate hydratase (EC 4.2.1.80) (2-hydroxypentadienoic acid hydratase)
