---
entity_id: "reaction.ecocyc.RXN-17799"
entity_type: "reaction"
name: "RXN-17799"
source_database: "EcoCyc"
source_id: "RXN-17799"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17799

`reaction.ecocyc.RXN-17799`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17799`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + CPD-14925 -> CPD-19153 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: ACETYL-COA + CPD-14925 -> CPD-19153 + CO-A; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), (3Z)-dec-3-enoyl-CoA (molecule.ecocyc.CPD-14925). Products: CoA (molecule.C00010), 3-oxo-(5Z)-dodecenoyl-CoA (molecule.ecocyc.CPD-19153).

## Annotation

ACETYL-COA + CPD-14925 -> CPD-19153 + CO-A; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19153|molecule.ecocyc.CPD-19153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-14925|molecule.ecocyc.CPD-14925]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17799`

## Notes

ACETYL-COA + CPD-14925 -> CPD-19153 + CO-A; direction=REVERSIBLE
