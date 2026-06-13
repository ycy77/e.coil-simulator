---
entity_id: "reaction.ecocyc.TRANS-RXN-352"
entity_type: "reaction"
name: "deoxycholate export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-352"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxycholate export

`reaction.ecocyc.TRANS-RXN-352`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-352`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141), multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202), multidrug efflux pump MdtEF-TolC (complex.ecocyc.TRANS-CPLX-204). Substrates: H+ (molecule.C00080), Deoxycholic acid (molecule.C04483). Products: H+ (molecule.C00080), Deoxycholic acid (molecule.C04483).

## Annotation

DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-352`

## Notes

DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
