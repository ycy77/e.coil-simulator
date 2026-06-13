---
entity_id: "reaction.ecocyc.FORMYLTHFDEFORMYL-RXN"
entity_type: "reaction"
name: "FORMYLTHFDEFORMYL-RXN"
source_database: "EcoCyc"
source_id: "FORMYLTHFDEFORMYL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FORMYLTHFDEFORMYL-RXN

`reaction.ecocyc.FORMYLTHFDEFORMYL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FORMYLTHFDEFORMYL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This enzyme uses water to cleave N10-formyltetrahydrofolate into tetrahydrofolate and formate . EcoCyc reaction equation: FORMYL-THF-GLU-N + WATER -> THF-GLU-N + FORMATE + PROTON; direction=LEFT-TO-RIGHT. This enzyme uses water to cleave N10-formyltetrahydrofolate into tetrahydrofolate and formate .

## Biological Role

Catalyzed by formyltetrahydrofolate deformylase (complex.ecocyc.FORMYLTHFDEFORMYL-CPLX). Substrates: H2O (molecule.C00001), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N). Products: Formate (molecule.C00058), H+ (molecule.C00080), THF-polyglutamate (molecule.C03541).

## Annotation

This enzyme uses water to cleave N10-formyltetrahydrofolate into tetrahydrofolate and formate .

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.FORMYLTHFDEFORMYL-CPLX|complex.ecocyc.FORMYLTHFDEFORMYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FORMYLTHFDEFORMYL-RXN`

## Notes

FORMYL-THF-GLU-N + WATER -> THF-GLU-N + FORMATE + PROTON; direction=LEFT-TO-RIGHT
