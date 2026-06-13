---
entity_id: "molecule.C00199"
entity_type: "small_molecule"
name: "D-Ribulose 5-phosphate"
source_database: "KEGG"
source_id: "C00199"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Ribulose 5-phosphate"
---

# D-Ribulose 5-phosphate

`molecule.C00199`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00199`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Ribulose 5-phosphate

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: D-Ribulose 5-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (15)

- `is_product_of` --> [[reaction.R01526|reaction.R01526]] `KEGG` `database` - C00002 + C00309 <=> C00008 + C00199
- `is_product_of` --> [[reaction.R01528|reaction.R01528]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_product_of` --> [[reaction.R01530|reaction.R01530]] `KEGG` `database` - C01112 <=> C00199
- `is_product_of` --> [[reaction.R10221|reaction.R10221]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.D-RIBULOKIN-RXN|reaction.ecocyc.D-RIBULOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DARAB5PISOM-RXN|reaction.ecocyc.DARAB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIB5PISOM-RXN|reaction.ecocyc.RIB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9952|reaction.ecocyc.RXN-9952]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7141|reaction.ecocyc.RXN0-7141]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01523|reaction.R01523]] `KEGG` `database` - C00002 + C00199 <=> C00008 + C01182
- `is_substrate_of` --> [[reaction.R01529|reaction.R01529]] `KEGG` `database` - C00199 <=> C00231
- `is_substrate_of` --> [[reaction.R07281|reaction.R07281]] `KEGG` `database` - C00199 <=> C15556 + C00058
- `is_substrate_of` --> [[reaction.ecocyc.DIOHBUTANONEPSYN-RXN|reaction.ecocyc.DIOHBUTANONEPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIBULP3EPIM-RXN|reaction.ecocyc.RIBULP3EPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN-9952|reaction.ecocyc.RXN-9952]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00199`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
