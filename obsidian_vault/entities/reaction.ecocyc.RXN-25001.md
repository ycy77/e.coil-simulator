---
entity_id: "reaction.ecocyc.RXN-25001"
entity_type: "reaction"
name: "RXN-25001"
source_database: "EcoCyc"
source_id: "RXN-25001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25001

`reaction.ecocyc.RXN-25001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25001`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-27507 + WATER -> UDP-N-ACETYLMURAMATE + SER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-27507 + WATER -> UDP-N-ACETYLMURAMATE + SER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), UDP-N-acetyl-α-D-muramoyl-L-serine (molecule.ecocyc.CPD-27507). Products: L-Serine (molecule.C00065), UDP-N-acetylmuramate (molecule.C01050).

## Annotation

CPD-27507 + WATER -> UDP-N-ACETYLMURAMATE + SER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27507|molecule.ecocyc.CPD-27507]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25001`

## Notes

CPD-27507 + WATER -> UDP-N-ACETYLMURAMATE + SER; direction=PHYSIOL-LEFT-TO-RIGHT
