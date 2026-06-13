---
entity_id: "molecule.C00131"
entity_type: "small_molecule"
name: "dATP"
source_database: "KEGG"
source_id: "C00131"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dATP"
  - "2'-Deoxyadenosine 5'-triphosphate"
  - "Deoxyadenosine 5'-triphosphate"
  - "Deoxyadenosine triphosphate"
---

# dATP

`molecule.C00131`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00131`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dATP; 2'-Deoxyadenosine 5'-triphosphate; Deoxyadenosine 5'-triphosphate; Deoxyadenosine triphosphate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: dATP; 2'-Deoxyadenosine 5'-triphosphate; Deoxyadenosine 5'-triphosphate; Deoxyadenosine triphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (19)

- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R01137|reaction.R01137]] `KEGG` `database` - C00002 + C00206 <=> C00008 + C00131
- `is_product_of` --> [[reaction.ecocyc.DADPKIN-RXN|reaction.ecocyc.DADPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7280|reaction.ecocyc.RXN0-7280]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-745|reaction.ecocyc.RXN0-745]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - C00131 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.R01138|reaction.R01138]] `KEGG` `database` - C00131 + C00022 <=> C00206 + C00074
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14290|reaction.ecocyc.RXN-14290]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-384|reaction.ecocyc.RXN0-384]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MANNOSE-ISOMERASE-RXN|reaction.ecocyc.MANNOSE-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN|reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-723|reaction.ecocyc.RXN0-723]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-724|reaction.ecocyc.RXN0-724]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-745|reaction.ecocyc.RXN0-745]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-746|reaction.ecocyc.RXN0-746]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN|reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00131`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
