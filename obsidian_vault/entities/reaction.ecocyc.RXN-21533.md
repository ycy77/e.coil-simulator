---
entity_id: "reaction.ecocyc.RXN-21533"
entity_type: "reaction"
name: "RXN-21533"
source_database: "EcoCyc"
source_id: "RXN-21533"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21533

`reaction.ecocyc.RXN-21533`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21533`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-23688 + ATP -> CPD-23690 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-23688 + ATP -> CPD-23690 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-glycero-L-galacto-octuluronate kinase (complex.ecocyc.CPLX0-8548). Substrates: ATP (molecule.C00002), L-glycero-L-galacto-octuluronate (molecule.ecocyc.CPD-23688). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-glycero-L-galacto-octuluronate-1-phosphate (molecule.ecocyc.CPD-23690).

## Annotation

CPD-23688 + ATP -> CPD-23690 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8548|complex.ecocyc.CPLX0-8548]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-23690|molecule.ecocyc.CPD-23690]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-23688|molecule.ecocyc.CPD-23688]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21533`

## Notes

CPD-23688 + ATP -> CPD-23690 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
