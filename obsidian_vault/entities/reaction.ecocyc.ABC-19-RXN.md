---
entity_id: "reaction.ecocyc.ABC-19-RXN"
entity_type: "reaction"
name: "ABC-19-RXN"
source_database: "EcoCyc"
source_id: "ABC-19-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-19-RXN

`reaction.ecocyc.ABC-19-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-19-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + CPD-3 + WATER -> ADP + Pi + CPD-3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-3 + WATER -> ADP + Pi + CPD-3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by molybdate ABC transporter (complex.ecocyc.ABC-19-CPLX), thiosulfate/sulfate ABC transporter (complex.ecocyc.ABC-7-CPLX), sulfate/thiosulfate ABC transporter (complex.ecocyc.ABC-70-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Molybdate (molecule.C06232). Products: ADP (molecule.C00008), H+ (molecule.C00080), Molybdate (molecule.C06232), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8171` molybdenum cofactor biosynthesis (EcoCyc)

## Annotation

ATP + CPD-3 + WATER -> ADP + Pi + CPD-3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8171` molybdenum cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.ABC-19-CPLX|complex.ecocyc.ABC-19-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06232|molecule.C06232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06232|molecule.C06232]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-19-RXN`

## Notes

ATP + CPD-3 + WATER -> ADP + Pi + CPD-3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
