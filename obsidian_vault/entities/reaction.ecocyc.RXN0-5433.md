---
entity_id: "reaction.ecocyc.RXN0-5433"
entity_type: "reaction"
name: "RXN0-5433"
source_database: "EcoCyc"
source_id: "RXN0-5433"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5433

`reaction.ecocyc.RXN0-5433`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5433`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEHYDRO-3-DEOXY-L-RHAMNONATE -> PYRUVATE + LACTALD; direction=REVERSIBLE EcoCyc reaction equation: DEHYDRO-3-DEOXY-L-RHAMNONATE -> PYRUVATE + LACTALD; direction=REVERSIBLE.

## Biological Role

Catalyzed by 2-keto-3-deoxy-L-rhamnonate aldolase (complex.ecocyc.CPLX0-7723). Substrates: 2-Dehydro-3-deoxy-L-rhamnonate (molecule.C03979). Products: Pyruvate (molecule.C00022), (S)-Lactaldehyde (molecule.C00424).

## Annotation

DEHYDRO-3-DEOXY-L-RHAMNONATE -> PYRUVATE + LACTALD; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7723|complex.ecocyc.CPLX0-7723]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03979|molecule.C03979]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5433`

## Notes

DEHYDRO-3-DEOXY-L-RHAMNONATE -> PYRUVATE + LACTALD; direction=REVERSIBLE
