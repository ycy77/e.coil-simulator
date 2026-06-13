---
entity_id: "reaction.ecocyc.MANNOSE-ISOMERASE-RXN"
entity_type: "reaction"
name: "MANNOSE-ISOMERASE-RXN"
source_database: "EcoCyc"
source_id: "MANNOSE-ISOMERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "D-mannose isomerase"
---

# MANNOSE-ISOMERASE-RXN

`reaction.ecocyc.MANNOSE-ISOMERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNOSE-ISOMERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15373 -> CPD-15382; direction=REVERSIBLE EcoCyc reaction equation: CPD-15373 -> CPD-15382; direction=REVERSIBLE.

## Biological Role

Catalyzed by sulfoquinovose isomerase (complex.ecocyc.CPLX0-7683). Substrates: aldehydo-D-mannose (molecule.ecocyc.CPD-15373). Products: keto-D-fructose (molecule.ecocyc.CPD-15382).

## Annotation

CPD-15373 -> CPD-15382; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7683|complex.ecocyc.CPLX0-7683]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15382|molecule.ecocyc.CPD-15382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15373|molecule.ecocyc.CPD-15373]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MANNOSE-ISOMERASE-RXN`

## Notes

CPD-15373 -> CPD-15382; direction=REVERSIBLE
