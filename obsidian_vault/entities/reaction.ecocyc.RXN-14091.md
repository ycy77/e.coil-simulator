---
entity_id: "reaction.ecocyc.RXN-14091"
entity_type: "reaction"
name: "RXN-14091"
source_database: "EcoCyc"
source_id: "RXN-14091"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14091

`reaction.ecocyc.RXN-14091`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14091`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3725 + WATER -> CPD-3724 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3725 + WATER -> CPD-3724 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cpdB (protein.P08331). Substrates: H2O (molecule.C00001), 2',3'-Cyclic UMP (molecule.C02355). Products: H+ (molecule.C00080), 3'-UMP (molecule.C01368).

## Annotation

CPD-3725 + WATER -> CPD-3724 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P08331|protein.P08331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01368|molecule.C01368]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02355|molecule.C02355]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14091`

## Notes

CPD-3725 + WATER -> CPD-3724 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
