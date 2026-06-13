---
entity_id: "molecule.C00063"
entity_type: "small_molecule"
name: "CTP"
source_database: "KEGG"
source_id: "C00063"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CTP"
  - "Cytidine 5'-triphosphate"
  - "Cytidine triphosphate"
---

# CTP

`molecule.C00063`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00063`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CTP; Cytidine 5'-triphosphate; Cytidine triphosphate

## Biological Role

Consumed as substrate in 16 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: CTP; Cytidine 5'-triphosphate; Cytidine triphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (29)

- `is_product_of` --> [[reaction.R00570|reaction.R00570]] `KEGG` `database` - C00002 + C00112 <=> C00008 + C00063
- `is_product_of` --> [[reaction.R00571|reaction.R00571]] `KEGG` `database` - C00002 + C00075 + C00014 <=> C00008 + C00009 + C00063
- `is_product_of` --> [[reaction.R00573|reaction.R00573]] `KEGG` `database` - C00002 + C00075 + C00064 + C00001 <=> C00008 + C00009 + C00063 + C00025
- `is_product_of` --> [[reaction.ecocyc.CDPKIN-RXN|reaction.ecocyc.CDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14325|reaction.ecocyc.RXN-14325]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00442|reaction.R00442]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00515|reaction.R00515]] `KEGG` `database` - C00063 + C00001 <=> C00055 + C00013
- `is_substrate_of` --> [[reaction.R00572|reaction.R00572]] `KEGG` `database` - C00063 + C00022 <=> C00112 + C00074
- `is_substrate_of` --> [[reaction.R00767|reaction.R00767]] `KEGG` `database` - C00063 + C00085 <=> C00112 + C00354
- `is_substrate_of` --> [[reaction.ecocyc.2.7.7.60-RXN|reaction.ecocyc.2.7.7.60-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CDPDIGLYSYN-RXN|reaction.ecocyc.CDPDIGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CPM-KDOSYNTH-RXN|reaction.ecocyc.CPM-KDOSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.P-PANTOCYSLIG-RXN|reaction.ecocyc.P-PANTOCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12195|reaction.ecocyc.RXN-12195]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22914|reaction.ecocyc.RXN-22914]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-383|reaction.ecocyc.RXN0-383]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5515|reaction.ecocyc.RXN0-5515]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6254|reaction.ecocyc.RXN0-6254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7080|reaction.ecocyc.RXN0-7080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-723|reaction.ecocyc.RXN0-723]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ASPCARBTRANS-RXN|reaction.ecocyc.ASPCARBTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5515|reaction.ecocyc.RXN0-5515]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00063`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
