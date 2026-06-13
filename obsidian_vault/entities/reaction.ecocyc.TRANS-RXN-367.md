---
entity_id: "reaction.ecocyc.TRANS-RXN-367"
entity_type: "reaction"
name: "erythromycin export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-367"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# erythromycin export

`reaction.ecocyc.TRANS-RXN-367`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-367`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

Erythromycins + PROTON -> Erythromycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Erythromycins + PROTON -> Erythromycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141), multidrug efflux pump MdtEF-TolC (complex.ecocyc.TRANS-CPLX-204). Substrates: H+ (molecule.C00080), an erythromycin (molecule.ecocyc.Erythromycins). Products: H+ (molecule.C00080), an erythromycin (molecule.ecocyc.Erythromycins).

## Annotation

Erythromycins + PROTON -> Erythromycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Erythromycins|molecule.ecocyc.Erythromycins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Erythromycins|molecule.ecocyc.Erythromycins]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-367`

## Notes

Erythromycins + PROTON -> Erythromycins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
