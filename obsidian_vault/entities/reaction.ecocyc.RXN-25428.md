---
entity_id: "reaction.ecocyc.RXN-25428"
entity_type: "reaction"
name: "RXN-25428"
source_database: "EcoCyc"
source_id: "RXN-25428"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25428

`reaction.ecocyc.RXN-25428`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25428`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-28028 -> CPD-28030 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-28028 -> CPD-28030 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 2-piperideine (molecule.ecocyc.CPD-28028). Products: H+ (molecule.C00080), (2R,3'R)-tetrahydroanabasine (molecule.ecocyc.CPD-28030).

## Annotation

CPD-28028 -> CPD-28030 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-28030|molecule.ecocyc.CPD-28030]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-28028|molecule.ecocyc.CPD-28028]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25428`

## Notes

CPD-28028 -> CPD-28030 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
