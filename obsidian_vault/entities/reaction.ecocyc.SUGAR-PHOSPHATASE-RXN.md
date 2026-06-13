---
entity_id: "reaction.ecocyc.SUGAR-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "SUGAR-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "SUGAR-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUGAR-PHOSPHATASE-RXN

`reaction.ecocyc.SUGAR-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUGAR-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

WATER + Sugar-Phosphate -> Sugar + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + Sugar-Phosphate -> Sugar + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), yidA (protein.P0A8Y5), yigL (protein.P27848), ybiV (protein.P75792), hxpA (protein.P77625). Substrates: H2O (molecule.C00001), a sugar phosphate (molecule.ecocyc.Sugar-Phosphate). Products: phosphate (molecule.ecocyc.Pi), a sugar (molecule.ecocyc.Sugar).

## Annotation

WATER + Sugar-Phosphate -> Sugar + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A8Y5|protein.P0A8Y5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27848|protein.P27848]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75792|protein.P75792]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77625|protein.P77625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Sugar|molecule.ecocyc.Sugar]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Sugar-Phosphate|molecule.ecocyc.Sugar-Phosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUGAR-PHOSPHATASE-RXN`

## Notes

WATER + Sugar-Phosphate -> Sugar + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
