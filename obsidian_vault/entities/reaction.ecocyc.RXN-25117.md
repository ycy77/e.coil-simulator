---
entity_id: "reaction.ecocyc.RXN-25117"
entity_type: "reaction"
name: "RXN-25117"
source_database: "EcoCyc"
source_id: "RXN-25117"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25117

`reaction.ecocyc.RXN-25117`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25117`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2039 + GLUTATHIONE -> CPD-27736 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2039 + GLUTATHIONE -> CPD-27736 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), antimonous acid (molecule.ecocyc.CPD0-2039). Products: H2O (molecule.C00001), antimony triglutathione (molecule.ecocyc.CPD-27736).

## Annotation

CPD0-2039 + GLUTATHIONE -> CPD-27736 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-27736|molecule.ecocyc.CPD-27736]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25117`

## Notes

CPD0-2039 + GLUTATHIONE -> CPD-27736 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
