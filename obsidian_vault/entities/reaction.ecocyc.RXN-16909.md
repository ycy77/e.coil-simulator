---
entity_id: "reaction.ecocyc.RXN-16909"
entity_type: "reaction"
name: "RXN-16909"
source_database: "EcoCyc"
source_id: "RXN-16909"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16909

`reaction.ecocyc.RXN-16909`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16909`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HCO3 + ATP -> CPD-18238 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HCO3 + ATP -> CPD-18238 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), carboxyphosphate (molecule.ecocyc.CPD-18238).

## Annotation

HCO3 + ATP -> CPD-18238 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18238|molecule.ecocyc.CPD-18238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16909`

## Notes

HCO3 + ATP -> CPD-18238 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
