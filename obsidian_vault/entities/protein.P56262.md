---
entity_id: "protein.P56262"
entity_type: "protein"
name: "ysgA"
source_database: "UniProt"
source_id: "P56262"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ysgA b3830 JW5853"
---

# ysgA

`protein.P56262`

## Static

- Type: `protein`
- Source: `UniProt:P56262`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Putative carboxymethylenebutenolidase (EC 3.1.1.45) (Dienelactone hydrolase) (DLH) Using the COFACTOR pipeline, which combines analyses based on structure and sequence similarities and protein-protein interaction networks, YsgA was predicted to catalyze a reaction similar to EC-3.1.1.45 .

## Biological Role

Catalyzes 2,3,5-trichlorodienelactone lactonohydrolase (reaction.R09136).

## Enriched Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00364` Fluorobenzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

Putative carboxymethylenebutenolidase (EC 3.1.1.45) (Dienelactone hydrolase) (DLH)

## Pathways

- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00364` Fluorobenzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R09136|reaction.R09136]] `KEGG` `database` - via EC:3.1.1.45

## Incoming Edges (1)

- `encodes` <-- [[gene.b3830|gene.b3830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P56262`
- `KEGG:ecj:JW5853;eco:b3830;ecoc:C3026_20725;`
- `GeneID:948320;`
- `GO:GO:0008806`
- `EC:3.1.1.45`

## Notes

Putative carboxymethylenebutenolidase (EC 3.1.1.45) (Dienelactone hydrolase) (DLH)
