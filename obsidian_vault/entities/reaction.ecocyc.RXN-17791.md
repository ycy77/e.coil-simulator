---
entity_id: "reaction.ecocyc.RXN-17791"
entity_type: "reaction"
name: "RXN-17791"
source_database: "EcoCyc"
source_id: "RXN-17791"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17791

`reaction.ecocyc.RXN-17791`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17791`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + CPD-19147 -> CO-A + CPD-19158; direction=REVERSIBLE EcoCyc reaction equation: ACETYL-COA + CPD-19147 -> CO-A + CPD-19158; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), (7Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-19147). Products: CoA (molecule.C00010), 3-oxo-(9Z)-hexadecenoyl-CoA (molecule.ecocyc.CPD-19158).

## Annotation

ACETYL-COA + CPD-19147 -> CO-A + CPD-19158; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19158|molecule.ecocyc.CPD-19158]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19147|molecule.ecocyc.CPD-19147]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17791`

## Notes

ACETYL-COA + CPD-19147 -> CO-A + CPD-19158; direction=REVERSIBLE
