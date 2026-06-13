---
entity_id: "reaction.ecocyc.D-RIBULOKIN-RXN"
entity_type: "reaction"
name: "D-RIBULOKIN-RXN"
source_database: "EcoCyc"
source_id: "D-RIBULOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-RIBULOKIN-RXN

`reaction.ecocyc.D-RIBULOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:D-RIBULOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-RIBULOSE + ATP -> PROTON + ADP + RIBULOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-RIBULOSE + ATP -> PROTON + ADP + RIBULOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), D-Ribulose (molecule.C00309). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Ribulose 5-phosphate (molecule.C00199).

## Enriched Pathways

- `ecocyc.RIBITOLUTIL-PWY` ribitol degradation I (EcoCyc)

## Annotation

D-RIBULOSE + ATP -> PROTON + ADP + RIBULOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.RIBITOLUTIL-PWY` ribitol degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00309|molecule.C00309]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:D-RIBULOKIN-RXN`

## Notes

D-RIBULOSE + ATP -> PROTON + ADP + RIBULOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT
