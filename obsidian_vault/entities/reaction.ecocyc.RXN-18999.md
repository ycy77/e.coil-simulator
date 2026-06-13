---
entity_id: "reaction.ecocyc.RXN-18999"
entity_type: "reaction"
name: "RXN-18999"
source_database: "EcoCyc"
source_id: "RXN-18999"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18999

`reaction.ecocyc.RXN-18999`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18999`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9190 + Pi -> GLC-1-P + GLYCERATE; direction=REVERSIBLE EcoCyc reaction equation: CPD-9190 + Pi -> GLC-1-P + GLYCERATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by ycjM (protein.P76041). Substrates: 2-O-(α-D-glucopyranosyl)-D-glycerate (molecule.ecocyc.CPD-9190), phosphate (molecule.ecocyc.Pi). Products: D-Glycerate (molecule.C00258), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P).

## Annotation

CPD-9190 + Pi -> GLC-1-P + GLYCERATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76041|protein.P76041]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9190|molecule.ecocyc.CPD-9190]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18999`

## Notes

CPD-9190 + Pi -> GLC-1-P + GLYCERATE; direction=REVERSIBLE
