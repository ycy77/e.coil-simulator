---
entity_id: "reaction.ecocyc.RXN0-7103"
entity_type: "reaction"
name: "RXN0-7103"
source_database: "EcoCyc"
source_id: "RXN0-7103"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7103

`reaction.ecocyc.RXN0-7103`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7103`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2558 + WATER -> CPD0-2559 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2558 + WATER -> CPD0-2559 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA thioesterase (complex.ecocyc.CPLX0-8127). Substrates: H2O (molecule.C00001), 2-hydroxycyclohepta-1,4,6-triene-1-carboxyl-CoA (molecule.ecocyc.CPD0-2558). Products: CoA (molecule.C00010), H+ (molecule.C00080), 2-hydroxycyclohepta-1,4,6-triene-1-carboxylate (molecule.ecocyc.CPD0-2559).

## Annotation

CPD0-2558 + WATER -> CPD0-2559 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8127|complex.ecocyc.CPLX0-8127]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2559|molecule.ecocyc.CPD0-2559]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2558|molecule.ecocyc.CPD0-2558]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7103`

## Notes

CPD0-2558 + WATER -> CPD0-2559 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
