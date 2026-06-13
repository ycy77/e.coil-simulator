---
entity_id: "molecule.C00627"
entity_type: "small_molecule"
name: "Pyridoxine phosphate"
source_database: "KEGG"
source_id: "C00627"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pyridoxine phosphate"
  - "Pyridoxine 5'-phosphate"
  - "Pyridoxine 5-phosphate"
  - "Pyridoxol 5'-phosphate"
---

# Pyridoxine phosphate

`molecule.C00627`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00627`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pyridoxine phosphate; Pyridoxine 5'-phosphate; Pyridoxine 5-phosphate; Pyridoxol 5'-phosphate EcoCyc common name: pyridoxine 5'-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: Pyridoxine phosphate; Pyridoxine 5'-phosphate; Pyridoxine 5-phosphate; Pyridoxol 5'-phosphate

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.R01909|reaction.R01909]] `KEGG` `database` - C00002 + C00314 <=> C00008 + C00627
- `is_product_of` --> [[reaction.R01911|reaction.R01911]] `KEGG` `database` - C00314 + C00009 <=> C00627 + C00001
- `is_product_of` --> [[reaction.R05838|reaction.R05838]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_product_of` --> [[reaction.ecocyc.PDXJ-RXN|reaction.ecocyc.PDXJ-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PNKIN-RXN|reaction.ecocyc.PNKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00278|reaction.R00278]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018
- `is_substrate_of` --> [[reaction.ecocyc.PNPOXI-RXN|reaction.ecocyc.PNPOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14181|reaction.ecocyc.RXN-14181]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GCVP-RXN|reaction.ecocyc.GCVP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00627`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
