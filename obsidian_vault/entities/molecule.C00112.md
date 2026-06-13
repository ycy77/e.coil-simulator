---
entity_id: "molecule.C00112"
entity_type: "small_molecule"
name: "CDP"
source_database: "KEGG"
source_id: "C00112"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CDP"
  - "Cytidine 5'-diphosphate"
  - "Cytidine diphosphate"
---

# CDP

`molecule.C00112`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00112`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CDP; Cytidine 5'-diphosphate; Cytidine diphosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: CDP; Cytidine 5'-diphosphate; Cytidine diphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (11)

- `activates` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00440|reaction.R00440]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112
- `is_product_of` --> [[reaction.R00512|reaction.R00512]] `KEGG` `database` - C00002 + C00055 <=> C00008 + C00112
- `is_product_of` --> [[reaction.R00572|reaction.R00572]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074
- `is_product_of` --> [[reaction.R00767|reaction.R00767]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_product_of` --> [[reaction.ecocyc.CDPREDUCT-RXN|reaction.ecocyc.CDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11832|reaction.ecocyc.RXN-11832]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12195|reaction.ecocyc.RXN-12195]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00570|reaction.R00570]] `KEGG` `database` - C00002 + C00112 <=> C00008 + C00063
- `is_substrate_of` --> [[reaction.ecocyc.CDPKIN-RXN|reaction.ecocyc.CDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00112`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
