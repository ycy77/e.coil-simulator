---
entity_id: "protein.P13482"
entity_type: "protein"
name: "treA"
source_database: "UniProt"
source_id: "P13482"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "treA osmA b1197 JW1186"
---

# treA

`protein.P13482`

## Static

- Type: `protein`
- Source: `UniProt:P13482`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Provides the cells with the ability to utilize trehalose at high osmolarity by splitting it into glucose molecules that can subsequently be taken up by the phosphotransferase-mediated uptake system. E. coli contains two trehalases: the periplasmic TreA (discussed here) and the cytoplasmic TREHALACYTO-MONOMER "TreF". Both enzymes catalyze the hydrolysis of trehalose into two molecules of D-glucose. Crystal structures of the enzyme alone and complexed with inhibitors have been solved . Expression of periplasmic trehalase is increased under conditions of high osmolarity and during the transition to stationary phase . TreA-mediated periplasmic trehalose recycling during nutrient stress is proposed to have regulatory implications via glucose-flux sensing . treA mutants accumulate extracellular trehalose under osmotic stress conditions . Reviews:

## Biological Role

Catalyzes alpha,alpha-trehalose glucohydrolase (reaction.R00010), TREHALA-RXN (reaction.ecocyc.TREHALA-RXN).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Provides the cells with the ability to utilize trehalose at high osmolarity by splitting it into glucose molecules that can subsequently be taken up by the phosphotransferase-mediated uptake system.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00010|reaction.R00010]] `KEGG` `database` - via EC:3.2.1.28
- `catalyzes` --> [[reaction.ecocyc.TREHALA-RXN|reaction.ecocyc.TREHALA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1197|gene.b1197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13482`
- `KEGG:ecj:JW1186;eco:b1197;ecoc:C3026_07040;`
- `GeneID:945757;`
- `GO:GO:0004555; GO:0005993; GO:0006974; GO:0030288; GO:0071474`
- `EC:3.2.1.28`

## Notes

Periplasmic trehalase (EC 3.2.1.28) (Alpha,alpha-trehalase) (Alpha,alpha-trehalose glucohydrolase) (Tre37A)
