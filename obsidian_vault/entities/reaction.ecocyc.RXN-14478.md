---
entity_id: "reaction.ecocyc.RXN-14478"
entity_type: "reaction"
name: "RXN-14478"
source_database: "EcoCyc"
source_id: "RXN-14478"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14478

`reaction.ecocyc.RXN-14478`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14478`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2483 + WATER -> CPD-15358 + N-23-DIHYDROXYBENZOYL-L-SERINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2483 + WATER -> CPD-15358 + N-23-DIHYDROXYBENZOYL-L-SERINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), N-(2,3-dihydroxybenzoyl)-L-serine trimer (molecule.ecocyc.CPD0-2483). Products: H+ (molecule.C00080), N-(2,3-dihydroxybenzoyl)-L-serine dimer (molecule.ecocyc.CPD-15358), N-(2,3-dihydroxybenzoyl)-L-serine (molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE).

## Annotation

CPD0-2483 + WATER -> CPD-15358 + N-23-DIHYDROXYBENZOYL-L-SERINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15358|molecule.ecocyc.CPD-15358]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE|molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2483|molecule.ecocyc.CPD0-2483]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14478`

## Notes

CPD0-2483 + WATER -> CPD-15358 + N-23-DIHYDROXYBENZOYL-L-SERINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
