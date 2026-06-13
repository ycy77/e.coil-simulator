---
entity_id: "molecule.C00088"
entity_type: "small_molecule"
name: "Nitrite"
source_database: "KEGG"
source_id: "C00088"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nitrite"
---

# Nitrite

`molecule.C00088`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00088`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nitrite Nitrous acid exists at physiological pH as the charged anion nitrite. pKa = 3.3 at 18 °C

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 13 reaction(s).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Nitrite

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (21)

- `is_product_of` --> [[reaction.R00787|reaction.R00787]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_product_of` --> [[reaction.R00792|reaction.R00792]] `KEGG` `database` - C00244 + 2 C06259 <=> C00088 + C00001 + 2 C06260
- `is_product_of` --> [[reaction.R05712|reaction.R05712]] `KEGG` `database` - C00014 + 2 C00001 + 6 C00125 <=> C00088 + 6 C00126 + 6 C00080
- `is_product_of` --> [[reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN|reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13854|reaction.ecocyc.RXN-13854]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23850|reaction.ecocyc.RXN-23850]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3501|reaction.ecocyc.RXN0-3501]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5242|reaction.ecocyc.RXN0-5242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6369|reaction.ecocyc.RXN0-6369]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6370|reaction.ecocyc.RXN0-6370]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7124|reaction.ecocyc.RXN0-7124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-137|reaction.ecocyc.TRANS-RXN-137]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-239|reaction.ecocyc.TRANS-RXN0-239]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.7.2.2-RXN|reaction.ecocyc.1.7.2.2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12827|reaction.ecocyc.RXN-12827]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18605|reaction.ecocyc.RXN-18605]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6954|reaction.ecocyc.RXN0-6954]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-137|reaction.ecocyc.TRANS-RXN-137]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-239|reaction.ecocyc.TRANS-RXN0-239]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3281|reaction.ecocyc.RXN0-3281]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P10903|protein.P10903]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00088`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
