---
entity_id: "reaction.ecocyc.RXN0-7014"
entity_type: "reaction"
name: "RXN0-7014"
source_database: "EcoCyc"
source_id: "RXN0-7014"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7014

`reaction.ecocyc.RXN0-7014`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7014`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1074 + ACETYL-COA -> CPD0-2518 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1074 + ACETYL-COA -> CPD0-2518 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phnO (protein.P16691). Substrates: Acetyl-CoA (molecule.C00024), (aminomethyl)phosphonate (molecule.ecocyc.CPD0-1074). Products: CoA (molecule.C00010), (acetamidomethyl)phosphonate (molecule.ecocyc.CPD0-2518).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Annotation

CPD0-1074 + ACETYL-COA -> CPD0-2518 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16691|protein.P16691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2518|molecule.ecocyc.CPD0-2518]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1074|molecule.ecocyc.CPD0-1074]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7014`

## Notes

CPD0-1074 + ACETYL-COA -> CPD0-2518 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
