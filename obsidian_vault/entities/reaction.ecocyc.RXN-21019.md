---
entity_id: "reaction.ecocyc.RXN-21019"
entity_type: "reaction"
name: "RXN-21019"
source_database: "EcoCyc"
source_id: "RXN-21019"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21019

`reaction.ecocyc.RXN-21019`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21019`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2040 + GLUTATHIONE -> CPD-22658 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2040 + GLUTATHIONE -> CPD-22658 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), arsenous acid (molecule.ecocyc.CPD0-2040). Products: H2O (molecule.C00001), arsenic triglutathione (molecule.ecocyc.CPD-22658).

## Annotation

CPD0-2040 + GLUTATHIONE -> CPD-22658 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22658|molecule.ecocyc.CPD-22658]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21019`

## Notes

CPD0-2040 + GLUTATHIONE -> CPD-22658 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
