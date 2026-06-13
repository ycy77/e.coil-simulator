---
entity_id: "reaction.ecocyc.RXN0-6954"
entity_type: "reaction"
name: "RXN0-6954"
source_database: "EcoCyc"
source_id: "RXN0-6954"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6954

`reaction.ecocyc.RXN0-6954`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6954`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NITRITE + PROTON + E- -> WATER + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NITRITE + PROTON + E- -> WATER + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Nitrite (molecule.C00088). Products: H2O (molecule.C00001), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

NITRITE + PROTON + E- -> WATER + AMMONIUM; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6954`

## Notes

NITRITE + PROTON + E- -> WATER + AMMONIUM; direction=LEFT-TO-RIGHT
