---
entity_id: "reaction.ecocyc.TRANS-RXN-8"
entity_type: "reaction"
name: "TRANS-RXN-8"
source_database: "EcoCyc"
source_id: "TRANS-RXN-8"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-8

`reaction.ecocyc.TRANS-RXN-8`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-8`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FE+2 -> FE+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FE+2 -> FE+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by divalent metal ion transporter ZupT (complex.ecocyc.CPLX0-8617). Substrates: Fe2+ (molecule.C14818). Products: Fe2+ (molecule.C14818).

## Annotation

FE+2 -> FE+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8617|complex.ecocyc.CPLX0-8617]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-8`

## Notes

FE+2 -> FE+2; direction=LEFT-TO-RIGHT
