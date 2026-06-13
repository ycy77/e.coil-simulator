---
entity_id: "reaction.ecocyc.ABC-35-RXN"
entity_type: "reaction"
name: "ABC-35-RXN"
source_database: "EcoCyc"
source_id: "ABC-35-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-35-RXN

`reaction.ecocyc.ABC-35-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-35-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + LEU + WATER -> ADP + Pi + LEU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + LEU + WATER -> ADP + Pi + LEU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by branched chain amino acid / phenylalanine ABC transporter (complex.ecocyc.ABC-15-CPLX), leucine / L-phenylalanine ABC transporter (complex.ecocyc.ABC-304-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Leucine (molecule.C00123). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Leucine (molecule.C00123), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + LEU + WATER -> ADP + Pi + LEU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-304-CPLX|complex.ecocyc.ABC-304-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-35-RXN`

## Notes

ATP + LEU + WATER -> ADP + Pi + LEU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
