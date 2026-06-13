---
entity_id: "reaction.ecocyc.TRANS-RXN-359"
entity_type: "reaction"
name: "ethidium export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-359"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ethidium export

`reaction.ecocyc.TRANS-RXN-359`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-359`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201), multidrug efflux pump MdtEF-TolC (complex.ecocyc.TRANS-CPLX-204). Substrates: H+ (molecule.C00080), ethidium (molecule.ecocyc.CPD0-1938). Products: H+ (molecule.C00080), ethidium (molecule.ecocyc.CPD0-1938).

## Annotation

CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-359`

## Notes

CPD0-1938 + PROTON -> CPD0-1938 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
