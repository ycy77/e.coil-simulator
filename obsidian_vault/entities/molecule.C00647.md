---
entity_id: "molecule.C00647"
entity_type: "small_molecule"
name: "Pyridoxamine phosphate"
source_database: "KEGG"
source_id: "C00647"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pyridoxamine phosphate"
  - "Pyridoxamine 5'-phosphate"
  - "Pyridoxamine 5-phosphate"
---

# Pyridoxamine phosphate

`molecule.C00647`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00647`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pyridoxamine phosphate; Pyridoxamine 5'-phosphate; Pyridoxamine 5-phosphate EcoCyc common name: pyridoxamine 5'-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: Pyridoxamine phosphate; Pyridoxamine 5'-phosphate; Pyridoxamine 5-phosphate

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.PYRAMKIN-RXN|reaction.ecocyc.PYRAMKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5240|reaction.ecocyc.RXN0-5240]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00277|reaction.R00277]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_substrate_of` --> [[reaction.ecocyc.PMPOXI-RXN|reaction.ecocyc.PMPOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7074|reaction.ecocyc.RXN0-7074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00647`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
