---
entity_id: "reaction.ecocyc.RXN-17955"
entity_type: "reaction"
name: "RXN-17955"
source_database: "EcoCyc"
source_id: "RXN-17955"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17955

`reaction.ecocyc.RXN-17955`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17955`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19235 + WATER -> CPD-19236 + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-19235 + WATER -> CPD-19236 + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnM (protein.P16689). Substrates: H2O (molecule.C00001), α-D-ribose 1-(acetamidomethylphosphonate) 5-triphosphate (molecule.ecocyc.CPD-19235). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), α-D-ribose-1-(2-N-acetamidomethylphosphonate) 5-phosphate (molecule.ecocyc.CPD-19236).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Annotation

CPD-19235 + WATER -> CPD-19236 + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16689|protein.P16689]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19236|molecule.ecocyc.CPD-19236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19235|molecule.ecocyc.CPD-19235]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17955`

## Notes

CPD-19235 + WATER -> CPD-19236 + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
