---
entity_id: "reaction.ecocyc.TRANS-RXN-355"
entity_type: "reaction"
name: "n-hexane export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-355"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# n-hexane export

`reaction.ecocyc.TRANS-RXN-355`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-355`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-9288 + PROTON -> CPD-9288 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9288 + PROTON -> CPD-9288 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141), multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201). Substrates: H+ (molecule.C00080), hexane (molecule.ecocyc.CPD-9288). Products: H+ (molecule.C00080), hexane (molecule.ecocyc.CPD-9288).

## Annotation

CPD-9288 + PROTON -> CPD-9288 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9288|molecule.ecocyc.CPD-9288]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9288|molecule.ecocyc.CPD-9288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-355`

## Notes

CPD-9288 + PROTON -> CPD-9288 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
