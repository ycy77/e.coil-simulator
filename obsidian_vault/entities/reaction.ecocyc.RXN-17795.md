---
entity_id: "reaction.ecocyc.RXN-17795"
entity_type: "reaction"
name: "RXN-17795"
source_database: "EcoCyc"
source_id: "RXN-17795"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17795

`reaction.ecocyc.RXN-17795`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17795`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + CPD-19148 -> CPD-19157 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: ACETYL-COA + CPD-19148 -> CPD-19157 + CO-A; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), (5Z)-dodecenoyl-CoA (molecule.ecocyc.CPD-19148). Products: CoA (molecule.C00010), 3-oxo-(7Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-19157).

## Annotation

ACETYL-COA + CPD-19148 -> CPD-19157 + CO-A; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19157|molecule.ecocyc.CPD-19157]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19148|molecule.ecocyc.CPD-19148]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17795`

## Notes

ACETYL-COA + CPD-19148 -> CPD-19157 + CO-A; direction=REVERSIBLE
