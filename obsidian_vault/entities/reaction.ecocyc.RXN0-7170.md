---
entity_id: "reaction.ecocyc.RXN0-7170"
entity_type: "reaction"
name: "RXN0-7170"
source_database: "EcoCyc"
source_id: "RXN0-7170"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7170

`reaction.ecocyc.RXN0-7170`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7170`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15056 + PRPP -> 5-P-BETA-D-RIBOSYL-AMINE + CROTONATE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15056 + PRPP -> 5-P-BETA-D-RIBOSYL-AMINE + CROTONATE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), (Z)-2-aminobutenoate (molecule.ecocyc.CPD-15056). Products: Diphosphate (molecule.C00013), 5-Phosphoribosylamine (molecule.C03090), crotonate (molecule.ecocyc.CROTONATE).

## Annotation

CPD-15056 + PRPP -> 5-P-BETA-D-RIBOSYL-AMINE + CROTONATE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03090|molecule.C03090]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CROTONATE|molecule.ecocyc.CROTONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15056|molecule.ecocyc.CPD-15056]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7170`

## Notes

CPD-15056 + PRPP -> 5-P-BETA-D-RIBOSYL-AMINE + CROTONATE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
