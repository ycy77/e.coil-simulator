---
entity_id: "molecule.C05924"
entity_type: "small_molecule"
name: "Molybdopterin"
source_database: "KEGG"
source_id: "C05924"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Molybdopterin"
  - "Pyranopterin"
  - "H2Dtpp-mP"
---

# Molybdopterin

`molecule.C05924`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05924`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Molybdopterin; Pyranopterin; H2Dtpp-mP In all molybdenum-containing enzymes except nitrogenase, the metal is coordinated to the organic cofactor molybdopterin (MPT), which also serves as the cofactor for tungsten-containing enzymes. When molybdenum is present, the compound is referred to as a CPD-15870. The MPT molecule is a substituted pterin ring that coordinates the metal through a dithiolene linkage. The name H2Dtpp-mP has been suggested as the systematic name for this compound .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

KEGG compound: Molybdopterin; Pyranopterin; H2Dtpp-mP

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN-8342|reaction.ecocyc.RXN-8342]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7198|reaction.ecocyc.RXN0-7198]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16457|reaction.ecocyc.RXN-16457]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21601|reaction.ecocyc.RXN-21601]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8344|reaction.ecocyc.RXN-8344]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05924`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
