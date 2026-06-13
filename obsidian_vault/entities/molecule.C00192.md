---
entity_id: "molecule.C00192"
entity_type: "small_molecule"
name: "Hydroxylamine"
source_database: "KEGG"
source_id: "C00192"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydroxylamine"
  - "NH2OH"
---

# Hydroxylamine

`molecule.C00192`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00192`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydroxylamine; NH2OH

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

KEGG compound: Hydroxylamine; NH2OH

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R00143|reaction.R00143]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_product_of` --> [[reaction.R00284|reaction.R00284]] `KEGG` `database` - C00028 + C00014 + C00001 <=> C00192 + C00030
- `is_product_of` --> [[reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN|reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17886|reaction.ecocyc.RXN-17886]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-3482|reaction.ecocyc.RXN-3482]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ALADEHYDCHLORO-RXN|reaction.ecocyc.ALADEHYDCHLORO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ASPDECARBOX-RXN|reaction.ecocyc.ASPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSPHASERDECARB-RXN|reaction.ecocyc.PHOSPHASERDECARB-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-10817|reaction.ecocyc.RXN-10817]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN|reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00192`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
