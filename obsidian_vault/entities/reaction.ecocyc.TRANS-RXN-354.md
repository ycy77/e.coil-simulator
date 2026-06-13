---
entity_id: "reaction.ecocyc.TRANS-RXN-354"
entity_type: "reaction"
name: "acriflavine efflux"
source_database: "EcoCyc"
source_id: "TRANS-RXN-354"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# acriflavine efflux

`reaction.ecocyc.TRANS-RXN-354`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-354`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-21070 + PROTON -> CPD-21070 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21070 + PROTON -> CPD-21070 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141), multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201). Substrates: H+ (molecule.C00080), 3,6-diamino-10-methylacridinium (molecule.ecocyc.CPD-21070). Products: H+ (molecule.C00080), 3,6-diamino-10-methylacridinium (molecule.ecocyc.CPD-21070).

## Annotation

CPD-21070 + PROTON -> CPD-21070 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21070|molecule.ecocyc.CPD-21070]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21070|molecule.ecocyc.CPD-21070]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-354`

## Notes

CPD-21070 + PROTON -> CPD-21070 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
