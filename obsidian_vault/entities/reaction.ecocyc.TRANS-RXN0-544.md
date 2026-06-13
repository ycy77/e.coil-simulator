---
entity_id: "reaction.ecocyc.TRANS-RXN0-544"
entity_type: "reaction"
name: "passive diffusion of ammonia"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-544"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# passive diffusion of ammonia

`reaction.ecocyc.TRANS-RXN0-544`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-544`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Pure phospholipid artificial membranes are permeable to gases, such as CO2, O2, N2 and NH3 . EcoCyc reaction equation: AMMONIA -> AMMONIA; direction=REVERSIBLE. Pure phospholipid artificial membranes are permeable to gases, such as CO2, O2, N2 and NH3 .

## Biological Role

Substrates: Ammonia (molecule.C00014). Products: Ammonia (molecule.C00014).

## Annotation

Pure phospholipid artificial membranes are permeable to gases, such as CO2, O2, N2 and NH3 .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-544`

## Notes

AMMONIA -> AMMONIA; direction=REVERSIBLE
