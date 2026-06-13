---
entity_id: "reaction.ecocyc.ABC-5-RXN"
entity_type: "reaction"
name: "ABC-5-RXN"
source_database: "EcoCyc"
source_id: "ABC-5-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-5-RXN

`reaction.ecocyc.ABC-5-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-5-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + COB-I-ALAMIN + WATER -> ADP + Pi + COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + COB-I-ALAMIN + WATER -> ADP + Pi + COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by vitamin B12 ABC transporter (complex.ecocyc.ABC-5-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Cob(I)alamin (molecule.C00853). Products: ADP (molecule.C00008), H+ (molecule.C00080), Cob(I)alamin (molecule.C00853), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + COB-I-ALAMIN + WATER -> ADP + Pi + COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-5-CPLX|complex.ecocyc.ABC-5-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-5-RXN`

## Notes

ATP + COB-I-ALAMIN + WATER -> ADP + Pi + COB-I-ALAMIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
