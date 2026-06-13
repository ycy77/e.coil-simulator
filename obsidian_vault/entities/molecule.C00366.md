---
entity_id: "molecule.C00366"
entity_type: "small_molecule"
name: "Urate"
source_database: "KEGG"
source_id: "C00366"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Urate"
  - "Uric acid"
---

# Urate

`molecule.C00366`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00366`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Urate; Uric acid Free uric acid is not found in urine. Instead, it is present as CPD-15041 and quadrurate salts . Excess accumulation of uric acid in the blood can lead to a type of arthritis known as gout, during which needle-like crystals of uric acid salts precipitate in joints, capillaries, skin, and other tissues. Saturation levels of uric acid in blood may also result in formation of sodium urate kidney stones.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Urate; Uric acid

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN0-901|reaction.ecocyc.RXN0-901]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-530|reaction.ecocyc.TRANS-RXN0-530]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-530|reaction.ecocyc.TRANS-RXN0-530]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00366`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
