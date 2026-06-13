---
entity_id: "reaction.ecocyc.3.1.3.68-RXN"
entity_type: "reaction"
name: "3.1.3.68-RXN"
source_database: "EcoCyc"
source_id: "3.1.3.68-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.3.68-RXN

`reaction.ecocyc.3.1.3.68-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.3.68-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

WATER + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE -> 2-DEOXY-D-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE -> 2-DEOXY-D-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), hxpB (protein.P77247). Substrates: H2O (molecule.C00001), 2-deoxy-D-glucose 6-phosphate (molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE). Products: 2-deoxy-D-glucose (molecule.ecocyc.2-DEOXY-D-GLUCOSE), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE -> 2-DEOXY-D-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77247|protein.P77247]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.2-DEOXY-D-GLUCOSE|molecule.ecocyc.2-DEOXY-D-GLUCOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE|molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.3.68-RXN`

## Notes

WATER + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE -> 2-DEOXY-D-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
