---
entity_id: "reaction.ecocyc.ATPASE-RXN"
entity_type: "reaction"
name: "ATPASE-RXN"
source_database: "EcoCyc"
source_id: "ATPASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ATPASE-RXN

`reaction.ecocyc.ATPASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ATPASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + WATER -> PROTON + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + WATER -> PROTON + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ATP-dependent helicase/uracil glycosylase Lhr (complex.ecocyc.CPLX0-8581), ychF (protein.P0ABU2), radD (protein.P33919). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + WATER -> PROTON + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[complex.ecocyc.CPLX0-3964|complex.ecocyc.CPLX0-3964]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[complex.ecocyc.CPLX0-8165|complex.ecocyc.CPLX0-8165]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8581|complex.ecocyc.CPLX0-8581]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABU2|protein.P0ABU2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33919|protein.P33919]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ATPASE-RXN`

## Notes

ATP + WATER -> PROTON + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
