---
entity_id: "reaction.ecocyc.TRANS-RXN0-501"
entity_type: "reaction"
name: "fructose-6-phosphate:phosphate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-501"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# fructose-6-phosphate:phosphate antiport

`reaction.ecocyc.TRANS-RXN0-501`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-501`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-18719 + Pi -> Pi + CPD-18719; direction=REVERSIBLE EcoCyc reaction equation: CPD-18719 + Pi -> Pi + CPD-18719; direction=REVERSIBLE.

## Biological Role

Catalyzed by uhpT (protein.P0AGC0). Substrates: D-Fructose 6-phosphate (molecule.C00085), phosphate (molecule.ecocyc.Pi). Products: D-Fructose 6-phosphate (molecule.C00085), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-18719 + Pi -> Pi + CPD-18719; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00085|molecule.C00085]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00085|molecule.C00085]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-501`

## Notes

CPD-18719 + Pi -> Pi + CPD-18719; direction=REVERSIBLE
