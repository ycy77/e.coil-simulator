---
entity_id: "molecule.C00144"
entity_type: "small_molecule"
name: "GMP"
source_database: "KEGG"
source_id: "C00144"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GMP"
  - "Guanosine 5'-phosphate"
  - "Guanosine monophosphate"
  - "Guanosine 5'-monophosphate"
  - "Guanylic acid"
---

# GMP

`molecule.C00144`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00144`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GMP; Guanosine 5'-phosphate; Guanosine monophosphate; Guanosine 5'-monophosphate; Guanylic acid

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 14 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: GMP; Guanosine 5'-phosphate; Guanosine monophosphate; Guanosine 5'-monophosphate; Guanylic acid

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (27)

- `is_product_of` --> [[reaction.R00426|reaction.R00426]] `KEGG` `database` - C00044 + C00001 <=> C00144 + C00013
- `is_product_of` --> [[reaction.R01134|reaction.R01134]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.COBALAMIN5PSYN-RXN|reaction.ecocyc.COBALAMIN5PSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GMP-REDUCT-RXN|reaction.ecocyc.GMP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GMP-SYN-GLUT-RXN|reaction.ecocyc.GMP-SYN-GLUT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GMP-SYN-NH3-RXN|reaction.ecocyc.GMP-SYN-NH3-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN|reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17905|reaction.ecocyc.RXN-17905]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17910|reaction.ecocyc.RXN-17910]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4121|reaction.ecocyc.RXN0-4121]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5108|reaction.ecocyc.RXN0-5108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6566|reaction.ecocyc.RXN0-6566]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-565|reaction.ecocyc.TRANS-RXN0-565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00332|reaction.R00332]] `KEGG` `database` - C00002 + C00144 <=> C00008 + C00035
- `is_substrate_of` --> [[reaction.R05223|reaction.R05223]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_substrate_of` --> [[reaction.ecocyc.GUANPRIBOSYLTRAN-RXN|reaction.ecocyc.GUANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7609|reaction.ecocyc.RXN-7609]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7352|reaction.ecocyc.RXN0-7352]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-565|reaction.ecocyc.TRANS-RXN0-565]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANPRIBOSYLTRAN-RXN|reaction.ecocyc.GUANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00144`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
