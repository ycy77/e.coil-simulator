---
entity_id: "reaction.ecocyc.RXN-17954"
entity_type: "reaction"
name: "RXN-17954"
source_database: "EcoCyc"
source_id: "RXN-17954"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17954

`reaction.ecocyc.RXN-17954`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17954`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2518 + ATP -> CPD-19235 + ADENINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2518 + ATP -> CPD-19235 + ADENINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnI (protein.P16687). Substrates: ATP (molecule.C00002), (acetamidomethyl)phosphonate (molecule.ecocyc.CPD0-2518). Products: Adenine (molecule.C00147), α-D-ribose 1-(acetamidomethylphosphonate) 5-triphosphate (molecule.ecocyc.CPD-19235).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Annotation

CPD0-2518 + ATP -> CPD-19235 + ADENINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16687|protein.P16687]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19235|molecule.ecocyc.CPD-19235]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2518|molecule.ecocyc.CPD0-2518]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17954`

## Notes

CPD0-2518 + ATP -> CPD-19235 + ADENINE; direction=LEFT-TO-RIGHT
