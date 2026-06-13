---
entity_id: "molecule.C00314"
entity_type: "small_molecule"
name: "Pyridoxine"
source_database: "KEGG"
source_id: "C00314"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pyridoxine"
  - "Pyridoxol"
---

# Pyridoxine

`molecule.C00314`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00314`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pyridoxine; Pyridoxol

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: Pyridoxine; Pyridoxol

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.RXN-14181|reaction.ecocyc.RXN-14181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-205|reaction.ecocyc.TRANS-RXN0-205]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01909|reaction.R01909]] `KEGG` `database` - C00002 + C00314 <=> C00008 + C00627
- `is_substrate_of` --> [[reaction.R01911|reaction.R01911]] `KEGG` `database` - C00314 + C00009 <=> C00627 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.PNKIN-RXN|reaction.ecocyc.PNKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN|reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-205|reaction.ecocyc.TRANS-RXN0-205]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.OHMETPYRKIN-RXN|reaction.ecocyc.OHMETPYRKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00314`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
