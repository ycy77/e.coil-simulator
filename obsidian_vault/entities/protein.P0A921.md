---
entity_id: "protein.P0A921"
entity_type: "protein"
name: "pldA"
source_database: "UniProt"
source_id: "P0A921"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:6397463}; Multi-pass membrane protein {ECO:0000269|PubMed:6397463}. Note=One of the very few enzymes located there."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pldA b3821 JW3794"
---

# pldA

`protein.P0A921`

## Static

- Type: `protein`
- Source: `UniProt:P0A921`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:6397463}; Multi-pass membrane protein {ECO:0000269|PubMed:6397463}. Note=One of the very few enzymes located there.

## Enriched Summary

FUNCTION: Has broad substrate specificity including hydrolysis of phosphatidylcholine with phospholipase A2 (EC 3.1.1.4) and phospholipase A1 (EC 3.1.1.32) activities. Strong expression leads to outer membrane breakdown and cell death; is dormant in normal growing cells. Required for efficient secretion of bacteriocins.

## Biological Role

Catalyzes phosphatidylcholine 2-acylhydrolase (reaction.R01313), phosphatidylcholine 1-acylhydrolase (reaction.R01314), phosphatidylcholine 2-acylhydrolase (reaction.R01315), phosphatidylcholine 1-acylhydrolase (reaction.R01316), phosphatidylcholine 2-acylhydrolase (reaction.R01317). Component of outer membrane phospholipase A (complex.ecocyc.CPLX0-7944).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Has broad substrate specificity including hydrolysis of phosphatidylcholine with phospholipase A2 (EC 3.1.1.4) and phospholipase A1 (EC 3.1.1.32) activities. Strong expression leads to outer membrane breakdown and cell death; is dormant in normal growing cells. Required for efficient secretion of bacteriocins.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00565` Ether lipid metabolism (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R01313|reaction.R01313]] `KEGG` `database` - via EC:3.1.1.4
- `catalyzes` --> [[reaction.R01314|reaction.R01314]] `KEGG` `database` - via EC:3.1.1.32
- `catalyzes` --> [[reaction.R01315|reaction.R01315]] `KEGG` `database` - via EC:3.1.1.4
- `catalyzes` --> [[reaction.R01316|reaction.R01316]] `KEGG` `database` - via EC:3.1.1.32
- `catalyzes` --> [[reaction.R01317|reaction.R01317]] `KEGG` `database` - via EC:3.1.1.4
- `is_component_of` --> [[complex.ecocyc.CPLX0-7944|complex.ecocyc.CPLX0-7944]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3821|gene.b3821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A921`
- `KEGG:ecj:JW3794;eco:b3821;ecoc:C3026_20680;`
- `GeneID:75174056;75204815;948307;`
- `GO:GO:0004620; GO:0004622; GO:0004623; GO:0005509; GO:0008970; GO:0009279; GO:0016042; GO:0042803; GO:0046471`
- `EC:3.1.1.32; 3.1.1.4`

## Notes

Phospholipase A1 (EC 3.1.1.32) (EC 3.1.1.4) (Detergent-resistant phospholipase A) (DR-phospholipase A) (Outer membrane phospholipase A) (OM PLA) (OMPLA) (Phosphatidylcholine 1-acylhydrolase)
