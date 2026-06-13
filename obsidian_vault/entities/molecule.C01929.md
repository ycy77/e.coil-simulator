---
entity_id: "molecule.C01929"
entity_type: "small_molecule"
name: "L-Histidinal"
source_database: "KEGG"
source_id: "C01929"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Histidinal"
---

# L-Histidinal

`molecule.C01929`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01929`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Histidinal EcoCyc common name: histidinal.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)

## Annotation

KEGG compound: L-Histidinal

## Pathways

- `eco00340` Histidine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.HISTOLDEHYD-RXN|reaction.ecocyc.HISTOLDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01163|reaction.R01163]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.HISTALDEHYD-RXN|reaction.ecocyc.HISTALDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01929`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
