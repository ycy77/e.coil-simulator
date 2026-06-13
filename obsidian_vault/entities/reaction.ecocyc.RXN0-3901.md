---
entity_id: "reaction.ecocyc.RXN0-3901"
entity_type: "reaction"
name: "RXN0-3901"
source_database: "EcoCyc"
source_id: "RXN0-3901"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3901

`reaction.ecocyc.RXN0-3901`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3901`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PUTRESCINE + GLT + ATP -> PROTON + GAMMA-GLUTAMYL-PUTRESCINE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PUTRESCINE + GLT + ATP -> PROTON + GAMMA-GLUTAMYL-PUTRESCINE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutamate-putrescine ligase (complex.ecocyc.CPLX0-7709). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), Putrescine (molecule.C00134). Products: ADP (molecule.C00008), H+ (molecule.C00080), gamma-L-Glutamylputrescine (molecule.C15699), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Annotation

PUTRESCINE + GLT + ATP -> PROTON + GAMMA-GLUTAMYL-PUTRESCINE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7709|complex.ecocyc.CPLX0-7709]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15699|molecule.C15699]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3901`

## Notes

PUTRESCINE + GLT + ATP -> PROTON + GAMMA-GLUTAMYL-PUTRESCINE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
