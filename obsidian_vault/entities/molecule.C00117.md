---
entity_id: "molecule.C00117"
entity_type: "small_molecule"
name: "D-Ribose 5-phosphate"
source_database: "KEGG"
source_id: "C00117"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Ribose 5-phosphate"
  - "Ribose 5-phosphate"
---

# D-Ribose 5-phosphate

`molecule.C00117`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00117`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Ribose 5-phosphate; Ribose 5-phosphate Please note that the structure shown here is that of CPD-15895, and is not accurate for this generic class, which also contains the furanose forms of D-ribose 5-phosphate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: D-Ribose 5-phosphate; Ribose 5-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (12)

- `activates` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00182|reaction.R00182]] `KEGG` `database` - C00020 + C00001 <=> C00147 + C00117
- `is_product_of` --> [[reaction.R00510|reaction.R00510]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117
- `is_product_of` --> [[reaction.R06863|reaction.R06863]] `KEGG` `database` - C05382 + C00068 <=> C13378 + C00117
- `is_product_of` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3.2.2.10-RXN|reaction.ecocyc.3.2.2.10-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PPENTOMUT-RXN|reaction.ecocyc.PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7352|reaction.ecocyc.RXN0-7352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PRPPSYN-RXN|reaction.ecocyc.PRPPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIB5PISOM-RXN|reaction.ecocyc.RIB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14509|reaction.ecocyc.RXN-14509]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDO-8PSYNTH-RXN|reaction.ecocyc.KDO-8PSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00117`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
