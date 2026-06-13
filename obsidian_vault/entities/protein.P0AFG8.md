---
entity_id: "protein.P0AFG8"
entity_type: "protein"
name: "aceE"
source_database: "UniProt"
source_id: "P0AFG8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aceE b0114 JW0110"
---

# aceE

`protein.P0AFG8`

## Static

- Type: `protein`
- Source: `UniProt:P0AFG8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the pyruvate dehydrogenase (PDH) complex, that catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2).

## Biological Role

Catalyzes pyruvate:thiamin diphosphate acetaldehydetransferase (decarboxylating) (reaction.R00014). Component of pyruvate dehydrogenase (complex.ecocyc.E1P-CPLX), pyruvate dehydrogenase (complex.ecocyc.PYRUVATEDEH-CPLX).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

FUNCTION: Component of the pyruvate dehydrogenase (PDH) complex, that catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2).

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00014|reaction.R00014]] `KEGG` `database` - via EC:1.2.4.1
- `is_component_of` --> [[complex.ecocyc.E1P-CPLX|complex.ecocyc.E1P-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=24

## Incoming Edges (1)

- `encodes` <-- [[gene.b0114|gene.b0114]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFG8`
- `KEGG:ecj:JW0110;eco:b0114;ecoc:C3026_00475;`
- `GeneID:75170013;75202071;944834;`
- `GO:GO:0000287; GO:0004739; GO:0005829; GO:0016020; GO:0030976; GO:0036094; GO:0042802; GO:0042803; GO:0042867; GO:0045254; GO:0060090`
- `EC:1.2.4.1`

## Notes

Pyruvate dehydrogenase E1 component (PDH E1 component) (EC 1.2.4.1)
