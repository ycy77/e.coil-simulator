---
entity_id: "reaction.ecocyc.ABC-15-RXN"
entity_type: "reaction"
name: "ABC-15-RXN"
source_database: "EcoCyc"
source_id: "ABC-15-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-15-RXN

`reaction.ecocyc.ABC-15-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-15-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + ILE + WATER -> ADP + Pi + ILE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + ILE + WATER -> ADP + Pi + ILE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by branched chain amino acid / phenylalanine ABC transporter (complex.ecocyc.ABC-15-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Isoleucine (molecule.C00407). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Isoleucine (molecule.C00407), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + ILE + WATER -> ADP + Pi + ILE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-15-RXN`

## Notes

ATP + ILE + WATER -> ADP + Pi + ILE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
