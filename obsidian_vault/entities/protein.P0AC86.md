---
entity_id: "protein.P0AC86"
entity_type: "protein"
name: "glgP"
source_database: "UniProt"
source_id: "P0AC86"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glgP glgY b3428 JW3391"
---

# glgP

`protein.P0AC86`

## Static

- Type: `protein`
- Source: `UniProt:P0AC86`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Phosphorylase is an important allosteric enzyme in carbohydrate metabolism. Enzymes from different sources differ in their regulatory mechanisms and in their natural substrates. However, all known phosphorylases share catalytic and structural properties.

## Biological Role

Catalyzes 1,4-alpha-D-glucan:orthophosphate alpha-D-glucosyltransferase (reaction.R02111), R06185 (reaction.R06185). Component of glycogen phosphorylase (complex.ecocyc.GLYCOPHOSPHORYL-CPLX).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Phosphorylase is an important allosteric enzyme in carbohydrate metabolism. Enzymes from different sources differ in their regulatory mechanisms and in their natural substrates. However, all known phosphorylases share catalytic and structural properties.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02111|reaction.R02111]] `KEGG` `database` - via EC:2.4.1.1
- `catalyzes` --> [[reaction.R06185|reaction.R06185]] `KEGG` `database` - via EC:2.4.1.1
- `is_component_of` --> [[complex.ecocyc.GLYCOPHOSPHORYL-CPLX|complex.ecocyc.GLYCOPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3428|gene.b3428]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC86`
- `KEGG:ecj:JW3391;eco:b3428;ecoc:C3026_18585;`
- `GeneID:93778561;947931;`
- `GO:GO:0005737; GO:0005980; GO:0008184; GO:0030170; GO:0042803`
- `EC:2.4.1.1`

## Notes

Glycogen phosphorylase (EC 2.4.1.1)
