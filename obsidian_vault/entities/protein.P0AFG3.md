---
entity_id: "protein.P0AFG3"
entity_type: "protein"
name: "sucA"
source_database: "UniProt"
source_id: "P0AFG3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sucA b0726 JW0715"
---

# sucA

`protein.P0AFG3`

## Static

- Type: `protein`
- Source: `UniProt:P0AFG3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: E1 component of the 2-oxoglutarate dehydrogenase (OGDH) complex which catalyzes the decarboxylation of 2-oxoglutarate, the first step in the conversion of 2-oxoglutarate to succinyl-CoA and CO(2). {ECO:0000269|PubMed:17367808}.

## Biological Role

Catalyzes R00621 (reaction.R00621). Component of 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX), 2-oxoglutarate decarboxylase, thiamine-requiring (complex.ecocyc.E1O).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

FUNCTION: E1 component of the 2-oxoglutarate dehydrogenase (OGDH) complex which catalyzes the decarboxylation of 2-oxoglutarate, the first step in the conversion of 2-oxoglutarate to succinyl-CoA and CO(2). {ECO:0000269|PubMed:17367808}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00621|reaction.R00621]] `KEGG` `database` - via EC:1.2.4.2
- `is_component_of` --> [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[complex.ecocyc.E1O|complex.ecocyc.E1O]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b0726|gene.b0726]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFG3`
- `KEGG:ecj:JW0715;eco:b0726;ecoc:C3026_03635;`
- `GeneID:75170715;75205557;945303;`
- `GO:GO:0000166; GO:0000287; GO:0004591; GO:0005737; GO:0005829; GO:0006099; GO:0030976; GO:0042802; GO:0045252`
- `EC:1.2.4.2`

## Notes

2-oxoglutarate dehydrogenase E1 component (EC 1.2.4.2) (Alpha-ketoglutarate dehydrogenase)
