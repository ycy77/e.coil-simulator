---
entity_id: "reaction.ecocyc.TRANS-RXN0-280"
entity_type: "reaction"
name: "Cu+ export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-280"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Cu+ export

`reaction.ecocyc.TRANS-RXN0-280`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-280`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

PROTON + CU+ -> PROTON + CU+; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CU+ -> PROTON + CU+; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by copper/silver export system (complex.ecocyc.CPLX0-1721). Substrates: H+ (molecule.C00080), Cu+ (molecule.ecocyc.CU_). Products: H+ (molecule.C00080), Cu+ (molecule.ecocyc.CU_).

## Annotation

PROTON + CU+ -> PROTON + CU+; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1721|complex.ecocyc.CPLX0-1721]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-280`

## Notes

PROTON + CU+ -> PROTON + CU+; direction=PHYSIOL-LEFT-TO-RIGHT
