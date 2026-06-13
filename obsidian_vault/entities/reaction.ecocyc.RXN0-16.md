---
entity_id: "reaction.ecocyc.RXN0-16"
entity_type: "reaction"
name: "RXN0-16"
source_database: "EcoCyc"
source_id: "RXN0-16"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-16

`reaction.ecocyc.RXN0-16`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-16`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MN+2 -> MN+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MN+2 -> MN+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by divalent metal ion transporter ZupT (complex.ecocyc.CPLX0-8617). Substrates: Mn2+ (molecule.ecocyc.MN_2). Products: Mn2+ (molecule.ecocyc.MN_2).

## Annotation

MN+2 -> MN+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8617|complex.ecocyc.CPLX0-8617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-16`

## Notes

MN+2 -> MN+2; direction=LEFT-TO-RIGHT
