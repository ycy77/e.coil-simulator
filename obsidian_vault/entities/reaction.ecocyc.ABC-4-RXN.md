---
entity_id: "reaction.ecocyc.ABC-4-RXN"
entity_type: "reaction"
name: "ABC-4-RXN"
source_database: "EcoCyc"
source_id: "ABC-4-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-4-RXN

`reaction.ecocyc.ABC-4-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-4-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + ARG + WATER -> ADP + Pi + ARG + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + ARG + WATER -> ADP + Pi + ARG + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine / arginine / ornithine ABC transporter (complex.ecocyc.ABC-3-CPLX), L-arginine ABC transporter (complex.ecocyc.ABC-4-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Arginine (molecule.C00062). Products: ADP (molecule.C00008), L-Arginine (molecule.C00062), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + ARG + WATER -> ADP + Pi + ARG + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ABC-3-CPLX|complex.ecocyc.ABC-3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-4-CPLX|complex.ecocyc.ABC-4-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-4-RXN`

## Notes

ATP + ARG + WATER -> ADP + Pi + ARG + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
