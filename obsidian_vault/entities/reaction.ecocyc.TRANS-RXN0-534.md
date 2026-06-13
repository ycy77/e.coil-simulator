---
entity_id: "reaction.ecocyc.TRANS-RXN0-534"
entity_type: "reaction"
name: "glyceraldehyde-3-phosphate:phosphate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-534"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glyceraldehyde-3-phosphate:phosphate antiport

`reaction.ecocyc.TRANS-RXN0-534`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-534`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-GLYCERALDEHYDE-3-PHOSPHATE + Pi -> L-GLYCERALDEHYDE-3-PHOSPHATE + Pi; direction=REVERSIBLE EcoCyc reaction equation: L-GLYCERALDEHYDE-3-PHOSPHATE + Pi -> L-GLYCERALDEHYDE-3-PHOSPHATE + Pi; direction=REVERSIBLE.

## Biological Role

Catalyzed by uhpT (protein.P0AGC0). Substrates: L-glyceraldehyde 3-phosphate (molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE), phosphate (molecule.ecocyc.Pi). Products: L-glyceraldehyde 3-phosphate (molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE), phosphate (molecule.ecocyc.Pi).

## Annotation

L-GLYCERALDEHYDE-3-PHOSPHATE + Pi -> L-GLYCERALDEHYDE-3-PHOSPHATE + Pi; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-534`

## Notes

L-GLYCERALDEHYDE-3-PHOSPHATE + Pi -> L-GLYCERALDEHYDE-3-PHOSPHATE + Pi; direction=REVERSIBLE
