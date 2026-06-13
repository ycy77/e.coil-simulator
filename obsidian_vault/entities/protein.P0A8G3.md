---
entity_id: "protein.P0A8G3"
entity_type: "protein"
name: "uxaC"
source_database: "UniProt"
source_id: "P0A8G3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uxaC ygjX ygjY ygjZ b3092 JW3063"
---

# uxaC

`protein.P0A8G3`

## Static

- Type: `protein`
- Source: `UniProt:P0A8G3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uronate isomerase (EC 5.3.1.12) (Glucuronate isomerase) (Uronic isomerase) Uronate isomerase catalyzes the initial step of isomerization of the alduronic to the keturonic acid in the glucuronate and galacturonate degradation pathways. Cofactor requirements of the enzyme are unclear; one of the earlier reports on purification of the enzyme states that Zn2+ inhibits the enzyme , while a later report states that uronate isomerase is a metalloenzyme, with Zn2+ as the likely physiologically relevant cofactor . Tagaturonate and fructuronate act as inducers ; production of the enzyme is under catabolite repression .

## Biological Role

Catalyzes GALACTUROISOM-RXN (reaction.ecocyc.GALACTUROISOM-RXN), GLUCUROISOM-RXN (reaction.ecocyc.GLUCUROISOM-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

Uronate isomerase (EC 5.3.1.12) (Glucuronate isomerase) (Uronic isomerase)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GALACTUROISOM-RXN|reaction.ecocyc.GALACTUROISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLUCUROISOM-RXN|reaction.ecocyc.GLUCUROISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3092|gene.b3092]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8G3`
- `KEGG:ecj:JW3063;eco:b3092;ecoc:C3026_16885;`
- `GeneID:86861242;93778895;947599;`
- `GO:GO:0008880; GO:0019698; GO:0042840`
- `EC:5.3.1.12`

## Notes

Uronate isomerase (EC 5.3.1.12) (Glucuronate isomerase) (Uronic isomerase)
