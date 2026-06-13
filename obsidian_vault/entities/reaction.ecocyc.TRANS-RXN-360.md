---
entity_id: "reaction.ecocyc.TRANS-RXN-360"
entity_type: "reaction"
name: "gentamicin export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-360"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# gentamicin export

`reaction.ecocyc.TRANS-RXN-360`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-360`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

Gentamycins + PROTON -> Gentamycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Gentamycins + PROTON -> Gentamycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrAD-TolC (complex.ecocyc.CPLX0-3932). Substrates: H+ (molecule.C00080), a gentamicin (molecule.ecocyc.Gentamycins). Products: H+ (molecule.C00080), a gentamicin (molecule.ecocyc.Gentamycins).

## Annotation

Gentamycins + PROTON -> Gentamycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3932|complex.ecocyc.CPLX0-3932]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Gentamycins|molecule.ecocyc.Gentamycins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Gentamycins|molecule.ecocyc.Gentamycins]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-360`

## Notes

Gentamycins + PROTON -> Gentamycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
