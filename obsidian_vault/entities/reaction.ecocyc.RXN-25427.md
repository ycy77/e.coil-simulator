---
entity_id: "reaction.ecocyc.RXN-25427"
entity_type: "reaction"
name: "RXN-25427"
source_database: "EcoCyc"
source_id: "RXN-25427"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25427

`reaction.ecocyc.RXN-25427`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25427`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-11764 + PROTON -> CPD-28028; direction=REVERSIBLE EcoCyc reaction equation: CPD-11764 + PROTON -> CPD-28028; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), 1-piperideine (molecule.ecocyc.CPD-11764). Products: 2-piperideine (molecule.ecocyc.CPD-28028).

## Annotation

CPD-11764 + PROTON -> CPD-28028; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-28028|molecule.ecocyc.CPD-28028]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-11764|molecule.ecocyc.CPD-11764]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25427`

## Notes

CPD-11764 + PROTON -> CPD-28028; direction=REVERSIBLE
