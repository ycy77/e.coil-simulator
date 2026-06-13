---
entity_id: "reaction.ecocyc.RXN-25434"
entity_type: "reaction"
name: "RXN-25434"
source_database: "EcoCyc"
source_id: "RXN-25434"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25434

`reaction.ecocyc.RXN-25434`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25434`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-11764 + PROTON -> CPD-28030; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-11764 + PROTON -> CPD-28030; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), 1-piperideine (molecule.ecocyc.CPD-11764). Products: (2R,3'R)-tetrahydroanabasine (molecule.ecocyc.CPD-28030).

## Annotation

CPD-11764 + PROTON -> CPD-28030; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-28030|molecule.ecocyc.CPD-28030]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-11764|molecule.ecocyc.CPD-11764]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25434`

## Notes

CPD-11764 + PROTON -> CPD-28030; direction=PHYSIOL-LEFT-TO-RIGHT
