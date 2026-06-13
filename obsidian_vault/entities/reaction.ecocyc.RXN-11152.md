---
entity_id: "reaction.ecocyc.RXN-11152"
entity_type: "reaction"
name: "RXN-11152"
source_database: "EcoCyc"
source_id: "RXN-11152"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11152

`reaction.ecocyc.RXN-11152`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11152`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

CPD-330 + WATER -> CPD0-1083 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-330 + WATER -> CPD0-1083 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by GLUCONOLACT-MONOMER (protein.ecocyc.GLUCONOLACT-MONOMER). Substrates: H2O (molecule.C00001), L-Galactono-1,4-lactone (molecule.C01115). Products: H+ (molecule.C00080), L-Galactonate (molecule.C15930).

## Annotation

CPD-330 + WATER -> CPD0-1083 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.ecocyc.GLUCONOLACT-MONOMER|protein.ecocyc.GLUCONOLACT-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15930|molecule.C15930]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01115|molecule.C01115]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11152`

## Notes

CPD-330 + WATER -> CPD0-1083 + PROTON; direction=REVERSIBLE
