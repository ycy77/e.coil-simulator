---
entity_id: "reaction.ecocyc.TRANS-RXN0-283"
entity_type: "reaction"
name: "TRANS-RXN0-283"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-283"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-283

`reaction.ecocyc.TRANS-RXN0-283`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-283`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-20903 + PROTON -> CPD-20903 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20903 + PROTON -> CPD-20903 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924). Substrates: H+ (molecule.C00080), cob(II)inamide (molecule.ecocyc.CPD-20903). Products: H+ (molecule.C00080), cob(II)inamide (molecule.ecocyc.CPD-20903).

## Annotation

CPD-20903 + PROTON -> CPD-20903 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20903|molecule.ecocyc.CPD-20903]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20903|molecule.ecocyc.CPD-20903]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-283`

## Notes

CPD-20903 + PROTON -> CPD-20903 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
