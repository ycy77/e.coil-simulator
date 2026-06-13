---
entity_id: "reaction.ecocyc.TRANS-RXN-33"
entity_type: "reaction"
name: "glucose-6-phosphate:phosphate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-33"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glucose-6-phosphate:phosphate antiport

`reaction.ecocyc.TRANS-RXN-33`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-33`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Pi + D-glucopyranose-6-phosphate -> D-glucopyranose-6-phosphate + Pi; direction=REVERSIBLE EcoCyc reaction equation: Pi + D-glucopyranose-6-phosphate -> D-glucopyranose-6-phosphate + Pi; direction=REVERSIBLE.

## Biological Role

Catalyzed by uhpT (protein.P0AGC0). Substrates: D-Glucose 6-phosphate (molecule.C00092), phosphate (molecule.ecocyc.Pi). Products: D-Glucose 6-phosphate (molecule.C00092), phosphate (molecule.ecocyc.Pi).

## Annotation

Pi + D-glucopyranose-6-phosphate -> D-glucopyranose-6-phosphate + Pi; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-33`

## Notes

Pi + D-glucopyranose-6-phosphate -> D-glucopyranose-6-phosphate + Pi; direction=REVERSIBLE
