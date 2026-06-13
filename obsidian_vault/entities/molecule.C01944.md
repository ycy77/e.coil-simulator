---
entity_id: "molecule.C01944"
entity_type: "small_molecule"
name: "Octanoyl-CoA"
source_database: "KEGG"
source_id: "C01944"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Octanoyl-CoA"
---

# Octanoyl-CoA

`molecule.C01944`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01944`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Octanoyl-CoA

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Octanoyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R03778|reaction.R03778]] `KEGG` `database` - C01944 + C00024 <=> C00010 + C05265
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13617|reaction.ecocyc.RXN-13617]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14229|reaction.ecocyc.RXN-14229]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01944`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
