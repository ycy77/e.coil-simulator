---
entity_id: "molecule.C00721"
entity_type: "small_molecule"
name: "Dextrin"
source_database: "KEGG"
source_id: "C00721"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dextrin"
---

# Dextrin

`molecule.C00721`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00721`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dextrin EcoCyc common name: a dextrin. Dextrins are a group of low-molecular-weight carbohydrates produced by the hydrolysis of the D-glucose polymers Starch or Glycogens glycogen. The term is usally used to describe a mixture of polymers of various sizes, where the glucose units are linked by either α-(1→4) or α-(1→6) glycosidic bonds. When the polymers were hydrolyzed sufficiently to produce chain lengths that are under 20 monomers, the mixture is referred to as Maltodextrins. The enzymatic degradation of starch by certain bacteria such as TAX-44252 results in formation of cyclical molecules known as Cyclodextrins cyclodextrins.

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: Dextrin

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R02108|reaction.R02108]] `KEGG` `database` - C00369 + C00001 <=> C00721 + C00369
- `is_product_of` --> [[reaction.R02112|reaction.R02112]] `KEGG` `database` - C00369 <=> C00721 + C00208

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00721`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
