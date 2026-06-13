---
entity_id: "molecule.C00286"
entity_type: "small_molecule"
name: "dGTP"
source_database: "KEGG"
source_id: "C00286"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dGTP"
  - "2'-Deoxyguanosine 5'-triphosphate"
  - "Deoxyguanosine 5'-triphosphate"
  - "Deoxyguanosine triphosphate"
---

# dGTP

`molecule.C00286`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00286`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dGTP; 2'-Deoxyguanosine 5'-triphosphate; Deoxyguanosine 5'-triphosphate; Deoxyguanosine triphosphate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: dGTP; 2'-Deoxyguanosine 5'-triphosphate; Deoxyguanosine 5'-triphosphate; Deoxyguanosine triphosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (11)

- `activates` --> [[reaction.ecocyc.RXN0-745|reaction.ecocyc.RXN0-745]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.DGDPKIN-RXN|reaction.ecocyc.DGDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-746|reaction.ecocyc.RXN0-746]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - C00286 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.ecocyc.DGTPTRIPHYDRO-RXN|reaction.ecocyc.DGTPTRIPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11410|reaction.ecocyc.RXN-11410]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-385|reaction.ecocyc.RXN0-385]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00286`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
