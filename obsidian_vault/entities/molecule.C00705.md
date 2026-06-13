---
entity_id: "molecule.C00705"
entity_type: "small_molecule"
name: "dCDP"
source_database: "KEGG"
source_id: "C00705"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dCDP"
  - "2'-Deoxycytidine diphosphate"
  - "2'-Deoxycytidine 5'-diphosphate"
---

# dCDP

`molecule.C00705`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00705`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dCDP; 2'-Deoxycytidine diphosphate; 2'-Deoxycytidine 5'-diphosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dCDP; 2'-Deoxycytidine diphosphate; 2'-Deoxycytidine 5'-diphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (6)

- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN-7913|reaction.ecocyc.RXN-7913]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CDPREDUCT-RXN|reaction.ecocyc.CDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DCDPKIN-RXN|reaction.ecocyc.DCDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00705`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
