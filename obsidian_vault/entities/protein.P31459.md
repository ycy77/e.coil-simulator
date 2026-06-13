---
entity_id: "protein.P31459"
entity_type: "protein"
name: "dgoK"
source_database: "UniProt"
source_id: "P31459"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgoK yidV b3693 JW3670"
---

# dgoK

`protein.P31459`

## Static

- Type: `protein`
- Source: `UniProt:P31459`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

2-dehydro-3-deoxygalactonokinase (EC 2.7.1.58) (2-keto-3-deoxy-galactonokinase) (2-oxo-3-deoxygalactonate kinase) 2-dehydro-3-deoxygalactonate kinase catalyzes the second reaction in the degradation of D-galactonate, the ATP-dependent phosphorylation of 2-dehydro-3-deoxygalactonate . Production of 2-dehydro-3-deoxygalactonate kinase is induced by growth on galactonate . The inducer is D-galactonate, and expression is subject to catabolite repression . DgoA: "D-galactonate"

## Biological Role

Catalyzes DEHYDDEOXGALACTKIN-RXN (reaction.ecocyc.DEHYDDEOXGALACTKIN-RXN).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

2-dehydro-3-deoxygalactonokinase (EC 2.7.1.58) (2-keto-3-deoxy-galactonokinase) (2-oxo-3-deoxygalactonate kinase)

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DEHYDDEOXGALACTKIN-RXN|reaction.ecocyc.DEHYDDEOXGALACTKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3693|gene.b3693]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31459`
- `KEGG:ecj:JW3670;eco:b3693;ecoc:C3026_20025;`
- `GeneID:948207;`
- `GO:GO:0005524; GO:0008671; GO:0034194`
- `EC:2.7.1.58`

## Notes

2-dehydro-3-deoxygalactonokinase (EC 2.7.1.58) (2-keto-3-deoxy-galactonokinase) (2-oxo-3-deoxygalactonate kinase)
