---
entity_id: "molecule.C00283"
entity_type: "small_molecule"
name: "Hydrogen sulfide"
source_database: "KEGG"
source_id: "C00283"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydrogen sulfide"
  - "Hydrogen-sulfide"
  - "H2S"
  - "Sulfide"
---

# Hydrogen sulfide

`molecule.C00283`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00283`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydrogen sulfide; Hydrogen-sulfide; H2S; Sulfide

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 14 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Hydrogen sulfide; Hydrogen-sulfide; H2S; Sulfide

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (20)

- `activates` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00782|reaction.R00782]] `KEGG` `database` - C00097 + C00001 <=> C00283 + C00022 + C00014
- `is_product_of` --> [[reaction.R07767|reaction.R07767]] `KEGG` `database` - C16236 + C22154 + 2 C00019 + 2 C22150 + 8 C00080 <=> C16832 + C22155 + 2 C00283 + 4 C14818 + 2 C00073 + 2 C05198 + 2 C22151
- `is_product_of` --> [[reaction.ecocyc.DCYSDESULF-RXN|reaction.ecocyc.DCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MERCAPYSTRANS-RXN|reaction.ecocyc.MERCAPYSTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-10851|reaction.ecocyc.RXN-10851]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15129|reaction.ecocyc.RXN-15129]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15348|reaction.ecocyc.RXN-15348]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18703|reaction.ecocyc.RXN-18703]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19381|reaction.ecocyc.RXN-19381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22286|reaction.ecocyc.RXN-22286]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6385|reaction.ecocyc.RXN0-6385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-310|reaction.ecocyc.TRANS-RXN-310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R07274|reaction.R07274]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.ACSERLY-RXN|reaction.ecocyc.ACSERLY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SULFITE-REDUCT-RXN|reaction.ecocyc.SULFITE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-310|reaction.ecocyc.TRANS-RXN-310]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00283`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
