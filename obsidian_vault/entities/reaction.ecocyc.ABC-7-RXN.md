---
entity_id: "reaction.ecocyc.ABC-7-RXN"
entity_type: "reaction"
name: "ABC-7-RXN"
source_database: "EcoCyc"
source_id: "ABC-7-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-7-RXN

`reaction.ecocyc.ABC-7-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-7-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + S2O3 + WATER -> ADP + Pi + S2O3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + S2O3 + WATER -> ADP + Pi + S2O3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thiosulfate/sulfate ABC transporter (complex.ecocyc.ABC-7-CPLX), sulfate/thiosulfate ABC transporter (complex.ecocyc.ABC-70-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Thiosulfate (molecule.C00320). Products: ADP (molecule.C00008), H+ (molecule.C00080), Thiosulfate (molecule.C00320), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + S2O3 + WATER -> ADP + Pi + S2O3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-7-RXN`

## Notes

ATP + S2O3 + WATER -> ADP + Pi + S2O3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
