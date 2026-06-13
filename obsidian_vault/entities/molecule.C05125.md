---
entity_id: "molecule.C05125"
entity_type: "small_molecule"
name: "2-(alpha-Hydroxyethyl)thiamine diphosphate"
source_database: "KEGG"
source_id: "C05125"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-(alpha-Hydroxyethyl)thiamine diphosphate"
  - "2-Hydroxyethyl-ThPP"
---

# 2-(alpha-Hydroxyethyl)thiamine diphosphate

`molecule.C05125`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05125`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-(alpha-Hydroxyethyl)thiamine diphosphate; 2-Hydroxyethyl-ThPP EcoCyc common name: 2-(α-hydroxyethyl)thiamine diphosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: 2-(alpha-Hydroxyethyl)thiamine diphosphate; 2-Hydroxyethyl-ThPP

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00014|reaction.R00014]] `KEGG` `database` - C00022 + C00068 <=> C05125 + C00011
- `is_product_of` --> [[reaction.R04672|reaction.R04672]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022
- `is_product_of` --> [[reaction.ecocyc.RXN-12583|reaction.ecocyc.RXN-12583]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04673|reaction.R04673]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12508|reaction.ecocyc.RXN-12508]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05125`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
