---
entity_id: "reaction.ecocyc.RXN-22604"
entity_type: "reaction"
name: "RXN-22604"
source_database: "EcoCyc"
source_id: "RXN-22604"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22604

`reaction.ecocyc.RXN-22604`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22604`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-LACTATE + PROTON -> CPD-24843; direction=REVERSIBLE EcoCyc reaction equation: D-LACTATE + PROTON -> CPD-24843; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), (R)-Lactate (molecule.C00256). Products: (R)-Lactate (molecule.C00256).

## Annotation

D-LACTATE + PROTON -> CPD-24843; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22604`

## Notes

D-LACTATE + PROTON -> CPD-24843; direction=REVERSIBLE
