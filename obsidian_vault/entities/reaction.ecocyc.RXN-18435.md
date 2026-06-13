---
entity_id: "reaction.ecocyc.RXN-18435"
entity_type: "reaction"
name: "RXN-18435"
source_database: "EcoCyc"
source_id: "RXN-18435"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18435

`reaction.ecocyc.RXN-18435`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18435`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-With-GO + WATER -> CPD-12427 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-With-GO + WATER -> CPD-12427 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutM (protein.P05523). Substrates: H2O (molecule.C00001), a 7,8-dihydro-8-oxoguanine in DNA (molecule.ecocyc.DNA-With-GO). Products: H+ (molecule.C00080), 7,8-dihydro-8-oxoguanine (molecule.ecocyc.CPD-12427), 4-oxo-2-pentenal (molecule.ecocyc.CPD-21221).

## Annotation

DNA-With-GO + WATER -> CPD-12427 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P05523|protein.P05523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12427|molecule.ecocyc.CPD-12427]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21221|molecule.ecocyc.CPD-21221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-With-GO|molecule.ecocyc.DNA-With-GO]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18435`

## Notes

DNA-With-GO + WATER -> CPD-12427 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
