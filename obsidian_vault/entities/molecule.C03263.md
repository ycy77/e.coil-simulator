---
entity_id: "molecule.C03263"
entity_type: "small_molecule"
name: "Coproporphyrinogen III"
source_database: "KEGG"
source_id: "C03263"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Coproporphyrinogen III"
---

# Coproporphyrinogen III

`molecule.C03263`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03263`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Coproporphyrinogen III

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Coproporphyrinogen III

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.UROGENDECARBOX-RXN|reaction.ecocyc.UROGENDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R06895|reaction.R06895]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_substrate_of` --> [[reaction.ecocyc.HEMN-RXN|reaction.ecocyc.HEMN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1461|reaction.ecocyc.RXN0-1461]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7325|reaction.ecocyc.RXN0-7325]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03263`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
