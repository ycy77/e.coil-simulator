---
entity_id: "reaction.ecocyc.TRANS-RXN-383"
entity_type: "reaction"
name: "TRANS-RXN-383"
source_database: "EcoCyc"
source_id: "TRANS-RXN-383"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-383

`reaction.ecocyc.TRANS-RXN-383`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-383`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-21777 + ATP + WATER -> CPD-21777 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21777 + ATP + WATER -> CPD-21777 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-methionine/D-methionine ABC transporter (complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), D-selenomethionine (molecule.ecocyc.CPD-21777). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-selenomethionine (molecule.ecocyc.CPD-21777), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-21777 + ATP + WATER -> CPD-21777 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21777|molecule.ecocyc.CPD-21777]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21777|molecule.ecocyc.CPD-21777]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-383`

## Notes

CPD-21777 + ATP + WATER -> CPD-21777 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
