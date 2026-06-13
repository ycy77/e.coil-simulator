---
entity_id: "reaction.ecocyc.RXN-22287"
entity_type: "reaction"
name: "RXN-22287"
source_database: "EcoCyc"
source_id: "RXN-22287"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22287

`reaction.ecocyc.RXN-22287`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22287`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-846 -> CPD-7046 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-846 -> CPD-7046 + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: hydrosulfide (molecule.ecocyc.CPD-846). Products: H+ (molecule.C00080), S2- (molecule.ecocyc.CPD-7046).

## Annotation

CPD-846 -> CPD-7046 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7046|molecule.ecocyc.CPD-7046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-846|molecule.ecocyc.CPD-846]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22287`

## Notes

CPD-846 -> CPD-7046 + PROTON; direction=REVERSIBLE
