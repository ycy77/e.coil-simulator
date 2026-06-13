---
entity_id: "molecule.C00522"
entity_type: "small_molecule"
name: "(R)-Pantoate"
source_database: "KEGG"
source_id: "C00522"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-Pantoate"
  - "Pantoate"
  - "Pantoic acid"
---

# (R)-Pantoate

`molecule.C00522`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00522`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-Pantoate; Pantoate; Pantoic acid

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: (R)-Pantoate; Pantoate; Pantoic acid

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN|reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN|reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN|reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00522`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
