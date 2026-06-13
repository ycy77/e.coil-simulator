---
entity_id: "reaction.ecocyc.RXN-16910"
entity_type: "reaction"
name: "RXN-16910"
source_database: "EcoCyc"
source_id: "RXN-16910"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16910

`reaction.ecocyc.RXN-16910`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16910`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-18238 + AMMONIUM -> CARBAMATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18238 + AMMONIUM -> CARBAMATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ammonium (molecule.ecocyc.AMMONIUM), carboxyphosphate (molecule.ecocyc.CPD-18238). Products: H+ (molecule.C00080), Carbamate (molecule.C01563), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-18238 + AMMONIUM -> CARBAMATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18238|molecule.ecocyc.CPD-18238]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16910`

## Notes

CPD-18238 + AMMONIUM -> CARBAMATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
