---
entity_id: "protein.P00490"
entity_type: "protein"
name: "malP"
source_database: "UniProt"
source_id: "P00490"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malP b3417 JW5689"
---

# malP

`protein.P00490`

## Static

- Type: `protein`
- Source: `UniProt:P00490`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Phosphorylase is an important allosteric enzyme in carbohydrate metabolism. Enzymes from different sources differ in their regulatory mechanisms and in their natural substrates. However, all known phosphorylases share catalytic and structural properties.

## Biological Role

Catalyzes 1,4-alpha-D-glucan:orthophosphate alpha-D-glucosyltransferase (reaction.R02111), R06185 (reaction.R06185). Component of maltodextrin phosphorylase (complex.ecocyc.MALDEXPHOSPHORYL-CPLX).

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
- `is_component_of` --> [[complex.ecocyc.MALDEXPHOSPHORYL-CPLX|complex.ecocyc.MALDEXPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3417|gene.b3417]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00490`
- `KEGG:ecj:JW5689;eco:b3417;ecoc:C3026_18535;`
- `GeneID:75202260;947922;`
- `GO:GO:0005737; GO:0005829; GO:0005980; GO:0008184; GO:0030170; GO:0030980; GO:0031220; GO:0042803`
- `EC:2.4.1.1`

## Notes

Maltodextrin phosphorylase (EC 2.4.1.1)
