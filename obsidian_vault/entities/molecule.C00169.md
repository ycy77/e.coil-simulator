---
entity_id: "molecule.C00169"
entity_type: "small_molecule"
name: "Carbamoyl phosphate"
source_database: "KEGG"
source_id: "C00169"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Carbamoyl phosphate"
---

# Carbamoyl phosphate

`molecule.C00169`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00169`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Carbamoyl phosphate

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

KEGG compound: Carbamoyl phosphate

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)

## Outgoing Edges (14)

- `is_product_of` --> [[reaction.R00150|reaction.R00150]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_product_of` --> [[reaction.R00575|reaction.R00575]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_product_of` --> [[reaction.ecocyc.CARBAMATE-KINASE-RXN|reaction.ecocyc.CARBAMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13202|reaction.ecocyc.RXN-13202]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14196|reaction.ecocyc.RXN-14196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22735|reaction.ecocyc.RXN-22735]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ASPCARBTRANS-RXN|reaction.ecocyc.ASPCARBTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ORNCARBAMTRANSFER-RXN|reaction.ecocyc.ORNCARBAMTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN|reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14552|reaction.ecocyc.RXN-14552]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17753|reaction.ecocyc.RXN-17753]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6435|reaction.ecocyc.RXN0-6435]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00169`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
