---
entity_id: "reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN"
entity_type: "reaction"
name: "BETA-PHOSPHOGLUCOMUTASE-RXN"
source_database: "EcoCyc"
source_id: "BETA-PHOSPHOGLUCOMUTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BETA-PHOSPHOGLUCOMUTASE-RXN

`reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BETA-PHOSPHOGLUCOMUTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-448 -> GLC-6-P; direction=REVERSIBLE EcoCyc reaction equation: CPD-448 -> GLC-6-P; direction=REVERSIBLE.

## Biological Role

Catalyzed by ycjU (protein.P77366). Substrates: beta-D-Glucose 1-phosphate (molecule.C00663). Products: beta-D-Glucose 6-phosphate (molecule.C01172).

## Annotation

CPD-448 -> GLC-6-P; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77366|protein.P77366]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00663|molecule.C00663]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BETA-PHOSPHOGLUCOMUTASE-RXN`

## Notes

CPD-448 -> GLC-6-P; direction=REVERSIBLE
