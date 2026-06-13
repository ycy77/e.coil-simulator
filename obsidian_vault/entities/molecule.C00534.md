---
entity_id: "molecule.C00534"
entity_type: "small_molecule"
name: "Pyridoxamine"
source_database: "KEGG"
source_id: "C00534"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pyridoxamine"
  - "PM"
---

# Pyridoxamine

`molecule.C00534`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00534`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pyridoxamine; PM

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: Pyridoxamine; PM

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-213|reaction.ecocyc.TRANS-RXN0-213]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PYRAMKIN-RXN|reaction.ecocyc.PYRAMKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-213|reaction.ecocyc.TRANS-RXN0-213]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00534`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
