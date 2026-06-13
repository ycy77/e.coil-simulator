---
entity_id: "reaction.ecocyc.TRANS-RXN0-276"
entity_type: "reaction"
name: "TRANS-RXN0-276"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-276"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-276

`reaction.ecocyc.TRANS-RXN0-276`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-276`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1189 -> CPD0-1189; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1189 -> CPD0-1189; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by undecaprenyl-phosphate-α-L-Ara4N flippase (complex.ecocyc.CPLX0-7720). Substrates: Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157). Products: Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157).

## Annotation

CPD0-1189 -> CPD0-1189; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7720|complex.ecocyc.CPLX0-7720]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C16157|molecule.C16157]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16157|molecule.C16157]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-276`

## Notes

CPD0-1189 -> CPD0-1189; direction=LEFT-TO-RIGHT
