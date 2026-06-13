---
entity_id: "reaction.ecocyc.ABC-25-RXN"
entity_type: "reaction"
name: "ABC-25-RXN"
source_database: "EcoCyc"
source_id: "ABC-25-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-25-RXN

`reaction.ecocyc.ABC-25-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-25-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + PUTRESCINE + WATER -> ADP + Pi + PUTRESCINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + PUTRESCINE + WATER -> ADP + Pi + PUTRESCINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by spermidine preferential ABC transporter (complex.ecocyc.ABC-24-CPLX), putrescine ABC transporter (complex.ecocyc.ABC-25-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Putrescine (molecule.C00134). Products: ADP (molecule.C00008), H+ (molecule.C00080), Putrescine (molecule.C00134), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + PUTRESCINE + WATER -> ADP + Pi + PUTRESCINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-25-CPLX|complex.ecocyc.ABC-25-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-25-RXN`

## Notes

ATP + PUTRESCINE + WATER -> ADP + Pi + PUTRESCINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
