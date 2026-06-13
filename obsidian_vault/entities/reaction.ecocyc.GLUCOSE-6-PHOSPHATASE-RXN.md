---
entity_id: "reaction.ecocyc.GLUCOSE-6-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "GLUCOSE-6-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "GLUCOSE-6-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCOSE-6-PHOSPHATASE-RXN

`reaction.ecocyc.GLUCOSE-6-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCOSE-6-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + GLC-6-P -> Pi + GLC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + GLC-6-P -> Pi + GLC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), beta-D-Glucose 6-phosphate (molecule.C01172). Products: beta-D-Glucose (molecule.C00221), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + GLC-6-P -> Pi + GLC; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUCOSE-6-PHOSPHATASE-RXN`

## Notes

WATER + GLC-6-P -> Pi + GLC; direction=PHYSIOL-LEFT-TO-RIGHT
