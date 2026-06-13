---
entity_id: "reaction.ecocyc.RXN0-7495"
entity_type: "reaction"
name: "RXN0-7495"
source_database: "EcoCyc"
source_id: "RXN0-7495"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7495

`reaction.ecocyc.RXN0-7495`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7495`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MALTOHEXAOSE + ATP + WATER -> ADP + MALTOHEXAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOHEXAOSE + ATP + WATER -> ADP + MALTOHEXAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltose ABC transporter (complex.ecocyc.ABC-16-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), maltohexaose (molecule.ecocyc.MALTOHEXAOSE). Products: ADP (molecule.C00008), H+ (molecule.C00080), maltohexaose (molecule.ecocyc.MALTOHEXAOSE), phosphate (molecule.ecocyc.Pi).

## Annotation

MALTOHEXAOSE + ATP + WATER -> ADP + MALTOHEXAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7495`

## Notes

MALTOHEXAOSE + ATP + WATER -> ADP + MALTOHEXAOSE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
