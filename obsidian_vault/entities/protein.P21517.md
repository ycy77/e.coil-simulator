---
entity_id: "protein.P21517"
entity_type: "protein"
name: "malZ"
source_database: "UniProt"
source_id: "P21517"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malZ b0403 JW0393"
---

# malZ

`protein.P21517`

## Static

- Type: `protein`
- Source: `UniProt:P21517`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: May play a role in regulating the intracellular level of maltotriose. Cleaves glucose from the reducing end of maltotriose and longer maltodextrins with a chain length of up to 7 glucose units.

## Biological Role

Catalyzes maltose glucohydrolase (reaction.R00028), sucrose glucohydrolase (reaction.R00801), sucrose alpha-glucohydrolase (reaction.R00802). Component of maltodextrin glucosidase (complex.ecocyc.CPLX0-8615).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: May play a role in regulating the intracellular level of maltotriose. Cleaves glucose from the reducing end of maltotriose and longer maltodextrins with a chain length of up to 7 glucose units.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00028|reaction.R00028]] `KEGG` `database` - via EC:3.2.1.20
- `catalyzes` --> [[reaction.R00801|reaction.R00801]] `KEGG` `database` - via EC:3.2.1.20
- `catalyzes` --> [[reaction.R00802|reaction.R00802]] `KEGG` `database` - via EC:3.2.1.20
- `is_component_of` --> [[complex.ecocyc.CPLX0-8615|complex.ecocyc.CPLX0-8615]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0403|gene.b0403]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21517`
- `KEGG:ecj:JW0393;eco:b0403;`
- `GeneID:949131;`
- `GO:GO:0000023; GO:0004558; GO:0005737; GO:0030980; GO:0042803`
- `EC:3.2.1.20`

## Notes

Maltodextrin glucosidase (EC 3.2.1.20) (Alpha-glucosidase)
