---
entity_id: "reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN"
entity_type: "reaction"
name: "GLUCOSE-1-PHOSPHAT-RXN"
source_database: "EcoCyc"
source_id: "GLUCOSE-1-PHOSPHAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCOSE-1-PHOSPHAT-RXN

`reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCOSE-1-PHOSPHAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

WATER + GLC-1-P -> Pi + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + GLC-1-P -> Pi + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glucose-1-phosphatase (complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX), yihX (protein.P0A8Y3). Substrates: H2O (molecule.C00001), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P). Products: D-Glucose (molecule.C00031), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)

## Annotation

WATER + GLC-1-P -> Pi + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX|complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A8Y3|protein.P0A8Y3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUCOSE-1-PHOSPHAT-RXN`

## Notes

WATER + GLC-1-P -> Pi + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
