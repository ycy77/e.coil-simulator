---
entity_id: "reaction.ecocyc.TRANS-RXN-351"
entity_type: "reaction"
name: "sulfadiazine export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-351"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# sulfadiazine export

`reaction.ecocyc.TRANS-RXN-351`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-351`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-20940 + PROTON -> CPD-20940 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20940 + PROTON -> CPD-20940 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative multidrug efflux pump MdtNOP (complex.ecocyc.CPLX0-7807). Substrates: H+ (molecule.C00080), sulfadiazine (molecule.ecocyc.CPD-20940). Products: H+ (molecule.C00080), sulfadiazine (molecule.ecocyc.CPD-20940).

## Annotation

CPD-20940 + PROTON -> CPD-20940 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7807|complex.ecocyc.CPLX0-7807]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20940|molecule.ecocyc.CPD-20940]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20940|molecule.ecocyc.CPD-20940]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-351`

## Notes

CPD-20940 + PROTON -> CPD-20940 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
