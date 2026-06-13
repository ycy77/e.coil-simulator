---
entity_id: "reaction.ecocyc.TRANS-RXN-363"
entity_type: "reaction"
name: "nalidixate export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# nalidixate export

`reaction.ecocyc.TRANS-RXN-363`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-363`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump EmrAB-TolC (complex.ecocyc.CPLX0-2121). Substrates: H+ (molecule.C00080), nalidixic acid (molecule.ecocyc.CPD-21025). Products: H+ (molecule.C00080), nalidixic acid (molecule.ecocyc.CPD-21025).

## Annotation

CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2121|complex.ecocyc.CPLX0-2121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21025|molecule.ecocyc.CPD-21025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21025|molecule.ecocyc.CPD-21025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-363`

## Notes

CPD-21025 + PROTON -> CPD-21025 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
