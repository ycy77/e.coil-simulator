---
entity_id: "reaction.ecocyc.TRANS-RXN0-536"
entity_type: "reaction"
name: "TRANS-RXN0-536"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-536"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-536

`reaction.ecocyc.TRANS-RXN0-536`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-536`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1551 -> CPD0-1551; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1551 -> CPD0-1551; direction=REVERSIBLE.

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: DL-glyceraldehyde (molecule.ecocyc.CPD0-1551). Products: DL-glyceraldehyde (molecule.ecocyc.CPD0-1551).

## Annotation

CPD0-1551 -> CPD0-1551; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1551|molecule.ecocyc.CPD0-1551]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1551|molecule.ecocyc.CPD0-1551]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-536`

## Notes

CPD0-1551 -> CPD0-1551; direction=REVERSIBLE
