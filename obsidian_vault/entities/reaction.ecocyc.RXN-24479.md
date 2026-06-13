---
entity_id: "reaction.ecocyc.RXN-24479"
entity_type: "reaction"
name: "RXN-24479"
source_database: "EcoCyc"
source_id: "RXN-24479"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24479

`reaction.ecocyc.RXN-24479`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24479`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ETR-Quinones + SELENITE + WATER -> ETR-Quinols + SELENATE; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ETR-Quinones + SELENITE + WATER -> ETR-Quinols + SELENATE; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by selenate reductase (complex.ecocyc.CPLX0-1601). Substrates: H2O (molecule.C00001), Selenite (molecule.C05684). Products: Selenate (molecule.C05697).

## Annotation

ETR-Quinones + SELENITE + WATER -> ETR-Quinols + SELENATE; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1601|complex.ecocyc.CPLX0-1601]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05697|molecule.C05697]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05684|molecule.C05684]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24479`

## Notes

ETR-Quinones + SELENITE + WATER -> ETR-Quinols + SELENATE; direction=PHYSIOL-RIGHT-TO-LEFT
