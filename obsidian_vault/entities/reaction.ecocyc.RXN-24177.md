---
entity_id: "reaction.ecocyc.RXN-24177"
entity_type: "reaction"
name: "RXN-24177"
source_database: "EcoCyc"
source_id: "RXN-24177"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24177

`reaction.ecocyc.RXN-24177`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24177`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dbpA (protein.P21693), hrpA (protein.P43329). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21693|protein.P21693]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P43329|protein.P43329]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24177`

## Notes

Wound-RNA + ATP + WATER -> Unwound-RNA + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
