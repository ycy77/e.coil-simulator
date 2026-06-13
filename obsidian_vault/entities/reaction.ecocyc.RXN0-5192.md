---
entity_id: "reaction.ecocyc.RXN0-5192"
entity_type: "reaction"
name: "RXN0-5192"
source_database: "EcoCyc"
source_id: "RXN0-5192"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5192

`reaction.ecocyc.RXN0-5192`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5192`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LYS -> CPD0-1032; direction=REVERSIBLE EcoCyc reaction equation: LYS -> CPD0-1032; direction=REVERSIBLE.

## Biological Role

Catalyzed by epmB (protein.P39280). Substrates: L-Lysine (molecule.C00047). Products: (R)-β-lysine (molecule.ecocyc.CPD0-1032).

## Annotation

LYS -> CPD0-1032; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P39280|protein.P39280]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1032|molecule.ecocyc.CPD0-1032]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5192`

## Notes

LYS -> CPD0-1032; direction=REVERSIBLE
