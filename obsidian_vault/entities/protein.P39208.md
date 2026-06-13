---
entity_id: "protein.P39208"
entity_type: "protein"
name: "idnK"
source_database: "UniProt"
source_id: "P39208"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "idnK gntV b4268 JW4225"
---

# idnK

`protein.P39208`

## Static

- Type: `protein`
- Source: `UniProt:P39208`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Thermosensitive gluconokinase (EC 2.7.1.12) (Gluconate kinase 1) E. coli encodes two D-gluconate kinases which can be distinguished by their thermal sensitivity. The idnK-encoded enzyme, described here, is thermosensitive , and its primary function is in the L-idonate degradation pathway . When grown on D-gluconate, the gntK-encoded thermostable enzyme is prevalent . Gluconokinase activity is induced by growth on gluconate . Expression of idnK is catabolite repressed and induced by L-idonate or 5-ketogluconate . An idnK insertion mutant is unable to grow on L-idonate or 5-ketogluconate as the sole source of carbon, and an idnK gntK double mutant is also unable to grow on D-gluconate as the sole source of carbon . GntV: "gluconate" IdnK: "idonate" Review:

## Biological Role

Catalyzes ATP:D-gluconate 6-phosphotransferase (reaction.R01737), GLUCONOKIN-RXN (reaction.ecocyc.GLUCONOKIN-RXN).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

Thermosensitive gluconokinase (EC 2.7.1.12) (Gluconate kinase 1)

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01737|reaction.R01737]] `KEGG` `database` - via EC:2.7.1.12
- `catalyzes` --> [[reaction.ecocyc.GLUCONOKIN-RXN|reaction.ecocyc.GLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4268|gene.b4268]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39208`
- `KEGG:ecj:JW4225;eco:b4268;ecoc:C3026_23020;`
- `GeneID:946066;`
- `GO:GO:0005524; GO:0019521; GO:0046183; GO:0046316`
- `EC:2.7.1.12`

## Notes

Thermosensitive gluconokinase (EC 2.7.1.12) (Gluconate kinase 1)
