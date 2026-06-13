---
entity_id: "reaction.ecocyc.TRANS-RXN-218"
entity_type: "reaction"
name: "TRANS-RXN-218"
source_database: "EcoCyc"
source_id: "TRANS-RXN-218"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-218

`reaction.ecocyc.TRANS-RXN-218`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-218`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON -> PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON -> PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

PROTON -> PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-218`

## Notes

PROTON -> PROTON; direction=LEFT-TO-RIGHT
