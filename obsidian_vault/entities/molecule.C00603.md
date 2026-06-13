---
entity_id: "molecule.C00603"
entity_type: "small_molecule"
name: "(S)-Ureidoglycolate"
source_database: "KEGG"
source_id: "C00603"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Ureidoglycolate"
  - "(-)-Ureidoglycolate"
---

# (S)-Ureidoglycolate

`molecule.C00603`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00603`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Ureidoglycolate; (-)-Ureidoglycolate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: (S)-Ureidoglycolate; (-)-Ureidoglycolate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.URUR-RXN|reaction.ecocyc.URUR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00776|reaction.R00776]] `KEGG` `database` - C00603 <=> C00048 + C00086
- `is_substrate_of` --> [[reaction.ecocyc.R165-RXN|reaction.ecocyc.R165-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7024|reaction.ecocyc.RXN0-7024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN|reaction.ecocyc.UREIDOGLYCOLATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00603`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
