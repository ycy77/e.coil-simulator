---
entity_id: "reaction.ecocyc.TRANS-RXN-356"
entity_type: "reaction"
name: "decanoate export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-356"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# decanoate export

`reaction.ecocyc.TRANS-RXN-356`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-356`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-3617 + PROTON -> CPD-3617 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3617 + PROTON -> CPD-3617 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201). Substrates: H+ (molecule.C00080), Decanoic acid (molecule.C01571). Products: H+ (molecule.C00080), Decanoic acid (molecule.C01571).

## Annotation

CPD-3617 + PROTON -> CPD-3617 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01571|molecule.C01571]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01571|molecule.C01571]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-356`

## Notes

CPD-3617 + PROTON -> CPD-3617 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
