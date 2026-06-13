---
entity_id: "reaction.ecocyc.RXN0-10"
entity_type: "reaction"
name: "RXN0-10"
source_database: "EcoCyc"
source_id: "RXN0-10"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-10

`reaction.ecocyc.RXN0-10`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-10`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CD+2 -> CD+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CD+2 -> CD+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by divalent metal ion transporter ZupT (complex.ecocyc.CPLX0-8617). Substrates: Cd2+ (molecule.ecocyc.CD_2). Products: Cd2+ (molecule.ecocyc.CD_2).

## Annotation

CD+2 -> CD+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8617|complex.ecocyc.CPLX0-8617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-10`

## Notes

CD+2 -> CD+2; direction=LEFT-TO-RIGHT
