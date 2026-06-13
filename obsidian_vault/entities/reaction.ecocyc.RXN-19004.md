---
entity_id: "reaction.ecocyc.RXN-19004"
entity_type: "reaction"
name: "RXN-19004"
source_database: "EcoCyc"
source_id: "RXN-19004"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19004

`reaction.ecocyc.RXN-19004`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19004`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-double-stranded-DNA-with-a-blunt-end + ATP + WATER + A-RECA-PROTEIN -> A-DOUBLE-STRANDED-DNA-WITH-A-3-OVERHANG + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-double-stranded-DNA-with-a-blunt-end + ATP + WATER + A-RECA-PROTEIN -> A-DOUBLE-STRANDED-DNA-WITH-A-3-OVERHANG + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by exodeoxyribonuclease V (complex.ecocyc.RECBCD). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

a-double-stranded-DNA-with-a-blunt-end + ATP + WATER + A-RECA-PROTEIN -> A-DOUBLE-STRANDED-DNA-WITH-A-3-OVERHANG + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.RECBCD|complex.ecocyc.RECBCD]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19004`

## Notes

a-double-stranded-DNA-with-a-blunt-end + ATP + WATER + A-RECA-PROTEIN -> A-DOUBLE-STRANDED-DNA-WITH-A-3-OVERHANG + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
