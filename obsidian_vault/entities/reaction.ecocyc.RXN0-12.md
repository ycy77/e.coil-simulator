---
entity_id: "reaction.ecocyc.RXN0-12"
entity_type: "reaction"
name: "RXN0-12"
source_database: "EcoCyc"
source_id: "RXN0-12"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-12

`reaction.ecocyc.RXN0-12`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-12`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ZN+2 -> ZN+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ZN+2 -> ZN+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by divalent metal ion transporter ZupT (complex.ecocyc.CPLX0-8617). Substrates: Zinc cation (molecule.C00038). Products: Zinc cation (molecule.C00038).

## Annotation

ZN+2 -> ZN+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8617|complex.ecocyc.CPLX0-8617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-10715|molecule.ecocyc.CPD-10715]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-12`

## Notes

ZN+2 -> ZN+2; direction=LEFT-TO-RIGHT
