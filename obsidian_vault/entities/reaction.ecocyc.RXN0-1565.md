---
entity_id: "reaction.ecocyc.RXN0-1565"
entity_type: "reaction"
name: "RXN0-1565"
source_database: "EcoCyc"
source_id: "RXN0-1565"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1565

`reaction.ecocyc.RXN0-1565`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1565`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

COB-I-ALAMIN + PROTON -> COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: COB-I-ALAMIN + PROTON -> COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924). Substrates: H+ (molecule.C00080), Cob(I)alamin (molecule.C00853). Products: H+ (molecule.C00080), Cob(I)alamin (molecule.C00853).

## Annotation

COB-I-ALAMIN + PROTON -> COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1565`

## Notes

COB-I-ALAMIN + PROTON -> COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
