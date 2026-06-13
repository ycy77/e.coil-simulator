---
entity_id: "reaction.ecocyc.RXN0-3"
entity_type: "reaction"
name: "RXN0-3"
source_database: "EcoCyc"
source_id: "RXN0-3"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3

`reaction.ecocyc.RXN0-3`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CYS + ATP + WATER -> CYS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + ATP + WATER -> CYS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by heme ABC transporter CydDC (complex.ecocyc.ABC-6-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Cysteine (molecule.C00097). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Cysteine (molecule.C00097), phosphate (molecule.ecocyc.Pi).

## Annotation

CYS + ATP + WATER -> CYS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-6-CPLX|complex.ecocyc.ABC-6-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3`

## Notes

CYS + ATP + WATER -> CYS + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
