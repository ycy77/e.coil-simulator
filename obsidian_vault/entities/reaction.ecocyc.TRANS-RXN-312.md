---
entity_id: "reaction.ecocyc.TRANS-RXN-312"
entity_type: "reaction"
name: "TRANS-RXN-312"
source_database: "EcoCyc"
source_id: "TRANS-RXN-312"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-312

`reaction.ecocyc.TRANS-RXN-312`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-312`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PHE + ATP + WATER -> PHE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHE + ATP + WATER -> PHE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by branched chain amino acid / phenylalanine ABC transporter (complex.ecocyc.ABC-15-CPLX), leucine / L-phenylalanine ABC transporter (complex.ecocyc.ABC-304-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Phenylalanine (molecule.C00079). Products: ADP (molecule.C00008), L-Phenylalanine (molecule.C00079), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

PHE + ATP + WATER -> PHE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-304-CPLX|complex.ecocyc.ABC-304-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-312`

## Notes

PHE + ATP + WATER -> PHE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
