---
entity_id: "reaction.ecocyc.RXN-16996"
entity_type: "reaction"
name: "RXN-16996"
source_database: "EcoCyc"
source_id: "RXN-16996"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16996

`reaction.ecocyc.RXN-16996`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16996`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON -> GLC-6-P + Phosphorylated-beta-phosphoglucomutase; direction=REVERSIBLE EcoCyc reaction equation: GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON -> GLC-6-P + Phosphorylated-beta-phosphoglucomutase; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), glucose-1,6-bisphosphate (molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE). Products: beta-D-Glucose 6-phosphate (molecule.C01172).

## Annotation

GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON -> GLC-6-P + Phosphorylated-beta-phosphoglucomutase; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE|molecule.ecocyc.GLUCOSE-16-DIPHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16996`

## Notes

GLUCOSE-16-DIPHOSPHATE + Beta-phosphoglucomutase + PROTON -> GLC-6-P + Phosphorylated-beta-phosphoglucomutase; direction=REVERSIBLE
