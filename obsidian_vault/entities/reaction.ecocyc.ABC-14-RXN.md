---
entity_id: "reaction.ecocyc.ABC-14-RXN"
entity_type: "reaction"
name: "ABC-14-RXN"
source_database: "EcoCyc"
source_id: "ABC-14-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-14-RXN

`reaction.ecocyc.ABC-14-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-14-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + HIS + WATER -> ADP + Pi + HIS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + HIS + WATER -> ADP + Pi + HIS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by histidine ABC transporter (complex.ecocyc.ABC-14-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Histidine (molecule.C00135). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Histidine (molecule.C00135), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + HIS + WATER -> ADP + Pi + HIS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-14-CPLX|complex.ecocyc.ABC-14-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-14-RXN`

## Notes

ATP + HIS + WATER -> ADP + Pi + HIS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
