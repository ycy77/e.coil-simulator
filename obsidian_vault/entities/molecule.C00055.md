---
entity_id: "molecule.C00055"
entity_type: "small_molecule"
name: "CMP"
source_database: "KEGG"
source_id: "C00055"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CMP"
  - "Cytidine-5'-monophosphate"
  - "Cytidylic acid"
---

# CMP

`molecule.C00055`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00055`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CMP; Cytidine-5'-monophosphate; Cytidylic acid

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 17 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: CMP; Cytidine-5'-monophosphate; Cytidylic acid

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (24)

- `is_product_of` --> [[reaction.R00513|reaction.R00513]] `KEGG` `database` - C00002 + C00475 <=> C00008 + C00055
- `is_product_of` --> [[reaction.R00515|reaction.R00515]] `KEGG` `database` - C00063 + C00001 <=> C00055 + C00013
- `is_product_of` --> [[reaction.R00517|reaction.R00517]] `KEGG` `database` - C00044 + C00475 <=> C00035 + C00055
- `is_product_of` --> [[reaction.R04658|reaction.R04658]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_product_of` --> [[reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN|reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CYTIKIN-RXN|reaction.ecocyc.CYTIKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.P-PANTOCYSLIG-RXN|reaction.ecocyc.P-PANTOCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSPHAGLYPSYN-RXN|reaction.ecocyc.PHOSPHAGLYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSPHASERSYN-RXN|reaction.ecocyc.PHOSPHASERSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11326|reaction.ecocyc.RXN-11326]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22915|reaction.ecocyc.RXN-22915]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-302|reaction.ecocyc.RXN0-302]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-383|reaction.ecocyc.RXN0-383]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7499|reaction.ecocyc.RXN0-7499]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00510|reaction.R00510]] `KEGG` `database` - C00055 + C00001 <=> C00380 + C00117
- `is_substrate_of` --> [[reaction.R00511|reaction.R00511]] `KEGG` `database` - C00055 + C00001 <=> C00475 + C00009
- `is_substrate_of` --> [[reaction.R00512|reaction.R00512]] `KEGG` `database` - C00002 + C00055 <=> C00008 + C00112
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11832|reaction.ecocyc.RXN-11832]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14026|reaction.ecocyc.RXN-14026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14065|reaction.ecocyc.RXN-14065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CPM-KDOSYNTH-RXN|reaction.ecocyc.CPM-KDOSYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00055`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
