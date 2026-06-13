---
entity_id: "molecule.C00130"
entity_type: "small_molecule"
name: "IMP"
source_database: "KEGG"
source_id: "C00130"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "IMP"
  - "Inosinic acid"
  - "Inosine monophosphate"
  - "Inosine 5'-monophosphate"
  - "Inosine 5'-phosphate"
  - "5'-Inosinate"
  - "5'-Inosinic acid"
  - "5'-Inosine monophosphate"
  - "5'-IMP"
---

# IMP

`molecule.C00130`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00130`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: IMP; Inosinic acid; Inosine monophosphate; Inosine 5'-monophosphate; Inosine 5'-phosphate; 5'-Inosinate; 5'-Inosinic acid; 5'-Inosine monophosphate; 5'-IMP

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: IMP; Inosinic acid; Inosine monophosphate; Inosine 5'-monophosphate; Inosine 5'-phosphate; 5'-Inosinate; 5'-Inosinic acid; 5'-Inosine monophosphate; 5'-IMP

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (21)

- `activates` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00720|reaction.R00720]] `KEGG` `database` - C00081 + C00001 <=> C00130 + C00013
- `is_product_of` --> [[reaction.ecocyc.INOSINEKIN-RXN|reaction.ecocyc.INOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6382|reaction.ecocyc.RXN0-6382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-566|reaction.ecocyc.TRANS-RXN0-566]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01134|reaction.R01134]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01135|reaction.R01135]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_substrate_of` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GMP-REDUCT-RXN|reaction.ecocyc.GMP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.IMPCYCLOHYDROLASE-RXN|reaction.ecocyc.IMPCYCLOHYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN|reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7607|reaction.ecocyc.RXN-7607]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-566|reaction.ecocyc.TRANS-RXN0-566]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN|reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PRPPAMIDOTRANS-RXN|reaction.ecocyc.PRPPAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SAICARSYN-RXN|reaction.ecocyc.SAICARSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00130`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
