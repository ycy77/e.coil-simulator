---
entity_id: "protein.P46859"
entity_type: "protein"
name: "gntK"
source_database: "UniProt"
source_id: "P46859"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gntK b3437 JW3400"
---

# gntK

`protein.P46859`

## Static

- Type: `protein`
- Source: `UniProt:P46859`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Thermoresistant gluconokinase (EC 2.7.1.12) (Gluconate kinase 2)

## Biological Role

Catalyzes ATP:D-gluconate 6-phosphotransferase (reaction.R01737). Component of D-gluconate kinase, thermostable (complex.ecocyc.GLUCONOKINII-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

Thermoresistant gluconokinase (EC 2.7.1.12) (Gluconate kinase 2)

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01737|reaction.R01737]] `KEGG` `database` - via EC:2.7.1.12
- `is_component_of` --> [[complex.ecocyc.GLUCONOKINII-CPLX|complex.ecocyc.GLUCONOKINII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3437|gene.b3437]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46859`
- `KEGG:ecj:JW3400;eco:b3437;ecoc:C3026_18625;`
- `GeneID:86948295;93778550;947937;`
- `GO:GO:0005524; GO:0005975; GO:0042803; GO:0046316`
- `EC:2.7.1.12`

## Notes

Thermoresistant gluconokinase (EC 2.7.1.12) (Gluconate kinase 2)
