---
entity_id: "reaction.ecocyc.TRANS-RXN0-264"
entity_type: "reaction"
name: "arsenite:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-264"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# arsenite:proton antiport

`reaction.ecocyc.TRANS-RXN0-264`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-264`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-763 -> PROTON + CPD-763; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-763 -> PROTON + CPD-763; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), arsenite (molecule.ecocyc.CPD-763). Products: H+ (molecule.C00080), arsenite (molecule.ecocyc.CPD-763).

## Annotation

PROTON + CPD-763 -> PROTON + CPD-763; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-264`

## Notes

PROTON + CPD-763 -> PROTON + CPD-763; direction=PHYSIOL-LEFT-TO-RIGHT
