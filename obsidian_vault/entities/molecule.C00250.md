---
entity_id: "molecule.C00250"
entity_type: "small_molecule"
name: "Pyridoxal"
source_database: "KEGG"
source_id: "C00250"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pyridoxal"
---

# Pyridoxal

`molecule.C00250`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00250`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pyridoxal

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: Pyridoxal

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.R00173|reaction.R00173]] `KEGG` `database` - C00018 + C00001 <=> C00250 + C00009
- `is_product_of` --> [[reaction.ecocyc.3.1.3.74-RXN|reaction.ecocyc.3.1.3.74-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN|reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-214|reaction.ecocyc.TRANS-RXN0-214]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00174|reaction.R00174]] `KEGG` `database` - C00002 + C00250 <=> C00008 + C00018
- `is_substrate_of` --> [[reaction.ecocyc.PYRIDOXKIN-RXN|reaction.ecocyc.PYRIDOXKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-214|reaction.ecocyc.TRANS-RXN0-214]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PYRIDOXKIN-RXN|reaction.ecocyc.PYRIDOXKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00250`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
