---
entity_id: "molecule.C00198"
entity_type: "small_molecule"
name: "D-Glucono-1,5-lactone"
source_database: "KEGG"
source_id: "C00198"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucono-1,5-lactone"
  - "Gluconic lactone"
  - "Gluconic acid lactone"
  - "1,5-Gluconolactone"
  - "delta-Gluconolactone"
  - "D-Gluconolactone"
  - "Gluconolactone"
---

# D-Glucono-1,5-lactone

`molecule.C00198`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00198`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucono-1,5-lactone; Gluconic lactone; Gluconic acid lactone; 1,5-Gluconolactone; delta-Gluconolactone; D-Gluconolactone; Gluconolactone

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: D-Glucono-1,5-lactone; Gluconic lactone; Gluconic acid lactone; 1,5-Gluconolactone; delta-Gluconolactone; D-Gluconolactone; Gluconolactone

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6373|reaction.ecocyc.RXN0-6373]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCONOLACT-RXN|reaction.ecocyc.GLUCONOLACT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6372|reaction.ecocyc.RXN0-6372]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00198`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
