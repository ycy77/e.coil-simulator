---
entity_id: "protein.P0AEX5"
entity_type: "protein"
name: "prkB"
source_database: "UniProt"
source_id: "P0AEX5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prkB yhfF b3355 JW3318"
---

# prkB

`protein.P0AEX5`

## Static

- Type: `protein`
- Source: `UniProt:P0AEX5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Probable phosphoribulokinase (PRK) (PRKase) (EC 2.7.1.19) (Phosphopentokinase) No information about this protein was found by a literature search conducted on August 19, 2020.

## Biological Role

Catalyzes ATP:D-ribulose-5-phosphate 1-phosphotransferase (reaction.R01523).

## Enriched Pathways

- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

Probable phosphoribulokinase (PRK) (PRKase) (EC 2.7.1.19) (Phosphopentokinase)

## Pathways

- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R01523|reaction.R01523]] `KEGG` `database` - via EC:2.7.1.19

## Incoming Edges (1)

- `encodes` <-- [[gene.b3355|gene.b3355]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEX5`
- `KEGG:ecj:JW3318;eco:b3355;ecoc:C3026_18220;`
- `GeneID:93778642;947862;`
- `GO:GO:0005524; GO:0005737; GO:0005975; GO:0008974`
- `EC:2.7.1.19`

## Notes

Probable phosphoribulokinase (PRK) (PRKase) (EC 2.7.1.19) (Phosphopentokinase)
