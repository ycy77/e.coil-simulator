---
entity_id: "reaction.ecocyc.ABC-20-RXN"
entity_type: "reaction"
name: "ABC-20-RXN"
source_database: "EcoCyc"
source_id: "ABC-20-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-20-RXN

`reaction.ecocyc.ABC-20-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-20-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NI+2 + ATP + WATER -> NI+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NI+2 + ATP + WATER -> NI+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Ni(2+) ABC transporter (complex.ecocyc.ABC-20-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Nickel(2+) (molecule.C19609). Products: ADP (molecule.C00008), H+ (molecule.C00080), Nickel(2+) (molecule.C19609), phosphate (molecule.ecocyc.Pi).

## Annotation

NI+2 + ATP + WATER -> NI+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-20-CPLX|complex.ecocyc.ABC-20-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-20-RXN`

## Notes

NI+2 + ATP + WATER -> NI+2 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
