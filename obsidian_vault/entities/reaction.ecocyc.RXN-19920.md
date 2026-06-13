---
entity_id: "reaction.ecocyc.RXN-19920"
entity_type: "reaction"
name: "RXN-19920"
source_database: "EcoCyc"
source_id: "RXN-19920"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19920

`reaction.ecocyc.RXN-19920`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19920`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-21533 + WATER -> Protein-L-lysine + CPD-14762; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21533 + WATER -> Protein-L-lysine + CPD-14762; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a [protein]-N6-[1,1-(5-adenosylyl-α-D-ribose-1,2-di-O-yl)ethyl]-L-lysine (molecule.ecocyc.CPD-21533). Products: Protein lysine (molecule.C02188), 2''-O-acetyl-ADP-ribose (molecule.ecocyc.CPD-14762).

## Annotation

CPD-21533 + WATER -> Protein-L-lysine + CPD-14762; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14762|molecule.ecocyc.CPD-14762]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21533|molecule.ecocyc.CPD-21533]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19920`

## Notes

CPD-21533 + WATER -> Protein-L-lysine + CPD-14762; direction=PHYSIOL-LEFT-TO-RIGHT
