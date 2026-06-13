---
entity_id: "reaction.ecocyc.TRANS-RXN0-502"
entity_type: "reaction"
name: "mannose-6-phosphate:phosphate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-502"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# mannose-6-phosphate:phosphate antiport

`reaction.ecocyc.TRANS-RXN0-502`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-502`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-15979 + Pi -> Pi + CPD-15979; direction=REVERSIBLE EcoCyc reaction equation: CPD-15979 + Pi -> Pi + CPD-15979; direction=REVERSIBLE.

## Biological Role

Catalyzed by uhpT (protein.P0AGC0). Substrates: D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979), phosphate (molecule.ecocyc.Pi). Products: D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-15979 + Pi -> Pi + CPD-15979; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGC0|protein.P0AGC0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-502`

## Notes

CPD-15979 + Pi -> Pi + CPD-15979; direction=REVERSIBLE
