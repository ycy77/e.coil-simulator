---
entity_id: "reaction.ecocyc.RXN-22607"
entity_type: "reaction"
name: "RXN-22607"
source_database: "EcoCyc"
source_id: "RXN-22607"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22607

`reaction.ecocyc.RXN-22607`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22607`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lactate + PROTON -> CPD-24845; direction=REVERSIBLE EcoCyc reaction equation: Lactate + PROTON -> CPD-24845; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), lactate (molecule.ecocyc.Lactate). Products: lactic acid (molecule.ecocyc.CPD-24845).

## Annotation

Lactate + PROTON -> CPD-24845; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-24845|molecule.ecocyc.CPD-24845]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lactate|molecule.ecocyc.Lactate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22607`

## Notes

Lactate + PROTON -> CPD-24845; direction=REVERSIBLE
