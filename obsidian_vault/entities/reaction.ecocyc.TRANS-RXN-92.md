---
entity_id: "reaction.ecocyc.TRANS-RXN-92"
entity_type: "reaction"
name: "dodecyl sulfate export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-92"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# dodecyl sulfate export

`reaction.ecocyc.TRANS-RXN-92`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-92`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-8876 + PROTON -> CPD-8876 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8876 + PROTON -> CPD-8876 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202). Substrates: H+ (molecule.C00080), dodecyl sulfate (molecule.ecocyc.CPD-8876). Products: H+ (molecule.C00080), dodecyl sulfate (molecule.ecocyc.CPD-8876).

## Annotation

CPD-8876 + PROTON -> CPD-8876 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8876|molecule.ecocyc.CPD-8876]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8876|molecule.ecocyc.CPD-8876]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-92`

## Notes

CPD-8876 + PROTON -> CPD-8876 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
