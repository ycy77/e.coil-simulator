---
entity_id: "reaction.ecocyc.RXN0-5220"
entity_type: "reaction"
name: "RXN0-5220"
source_database: "EcoCyc"
source_id: "RXN0-5220"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5220

`reaction.ecocyc.RXN0-5220`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5220`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OH + PROTON -> WATER; direction=REVERSIBLE EcoCyc reaction equation: OH + PROTON -> WATER; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), OH- (molecule.ecocyc.OH). Products: H2O (molecule.C00001).

## Annotation

OH + PROTON -> WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.OH|molecule.ecocyc.OH]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5220`

## Notes

OH + PROTON -> WATER; direction=REVERSIBLE
