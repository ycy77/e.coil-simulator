---
entity_id: "reaction.ecocyc.RXN-22605"
entity_type: "reaction"
name: "RXN-22605"
source_database: "EcoCyc"
source_id: "RXN-22605"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22605

`reaction.ecocyc.RXN-22605`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22605`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-LACTATE + PROTON -> CPD-24844; direction=LEFT-TO-RIGHT EcoCyc reaction equation: L-LACTATE + PROTON -> CPD-24844; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), (S)-Lactate (molecule.C00186). Products: (S)-Lactate (molecule.C00186).

## Annotation

L-LACTATE + PROTON -> CPD-24844; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22605`

## Notes

L-LACTATE + PROTON -> CPD-24844; direction=LEFT-TO-RIGHT
