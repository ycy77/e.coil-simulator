---
entity_id: "reaction.ecocyc.PANTETHEINE-KINASE-RXN"
entity_type: "reaction"
name: "PANTETHEINE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "PANTETHEINE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PANTETHEINE-KINASE-RXN

`reaction.ecocyc.PANTETHEINE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PANTETHEINE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-511 + ATP -> PANTETHEINE-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-511 + ATP -> PANTETHEINE-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pantothenate kinase / pantetheine kinase (complex.ecocyc.PANTOTHENATE-KIN-CPLX). Substrates: ATP (molecule.C00002), Pantetheine (molecule.C00831). Products: ADP (molecule.C00008), H+ (molecule.C00080), Pantetheine 4'-phosphate (molecule.C01134).

## Annotation

CPD-511 + ATP -> PANTETHEINE-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.PANTOTHENATE-KIN-CPLX|complex.ecocyc.PANTOTHENATE-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01134|molecule.C01134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00831|molecule.C00831]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PANTETHEINE-KINASE-RXN`

## Notes

CPD-511 + ATP -> PANTETHEINE-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
