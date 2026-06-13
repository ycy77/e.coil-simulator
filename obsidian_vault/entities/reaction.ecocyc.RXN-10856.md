---
entity_id: "reaction.ecocyc.RXN-10856"
entity_type: "reaction"
name: "RXN-10856"
source_database: "EcoCyc"
source_id: "RXN-10856"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10856

`reaction.ecocyc.RXN-10856`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10856`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDRO-NEO-PTERIN -> CPD-11770; direction=REVERSIBLE EcoCyc reaction equation: DIHYDRO-NEO-PTERIN -> CPD-11770; direction=REVERSIBLE.

## Biological Role

Catalyzed by dihydroneopterin aldolase (complex.ecocyc.CPLX0-3936). Substrates: 7,8-Dihydroneopterin (molecule.C04874). Products: 7,8-Dihydromonapterin (molecule.C21008).

## Annotation

DIHYDRO-NEO-PTERIN -> CPD-11770; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3936|complex.ecocyc.CPLX0-3936]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C21008|molecule.C21008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04874|molecule.C04874]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10856`

## Notes

DIHYDRO-NEO-PTERIN -> CPD-11770; direction=REVERSIBLE
