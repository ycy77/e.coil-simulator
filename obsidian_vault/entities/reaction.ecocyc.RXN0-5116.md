---
entity_id: "reaction.ecocyc.RXN0-5116"
entity_type: "reaction"
name: "RXN0-5116"
source_database: "EcoCyc"
source_id: "RXN0-5116"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5116

`reaction.ecocyc.RXN0-5116`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5116`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-RIBULOSE + ATP -> PROTON + L-RIBULOSE-5-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-RIBULOSE + ATP -> PROTON + L-RIBULOSE-5-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribulokinase (complex.ecocyc.RIBULOKIN-CPLX). Substrates: ATP (molecule.C00002), L-Ribulose (molecule.C00508). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Ribulose 5-phosphate (molecule.C01101).

## Enriched Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)

## Annotation

L-RIBULOSE + ATP -> PROTON + L-RIBULOSE-5-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.RIBULOKIN-CPLX|complex.ecocyc.RIBULOKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01101|molecule.C01101]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00508|molecule.C00508]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5116`

## Notes

L-RIBULOSE + ATP -> PROTON + L-RIBULOSE-5-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
