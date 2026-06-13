---
entity_id: "reaction.ecocyc.TRANS-RXN-381"
entity_type: "reaction"
name: "TRANS-RXN-381"
source_database: "EcoCyc"
source_id: "TRANS-RXN-381"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-381

`reaction.ecocyc.TRANS-RXN-381`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-381`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-27 -> CPD-27; direction=REVERSIBLE EcoCyc reaction equation: CPD-27 -> CPD-27; direction=REVERSIBLE.

## Biological Role

Catalyzed by formate channel FocA (complex.ecocyc.CPLX0-7843). Substrates: phosphinate (molecule.ecocyc.CPD-27). Products: phosphinate (molecule.ecocyc.CPD-27).

## Annotation

CPD-27 -> CPD-27; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7843|complex.ecocyc.CPLX0-7843]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-27|molecule.ecocyc.CPD-27]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27|molecule.ecocyc.CPD-27]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-381`

## Notes

CPD-27 -> CPD-27; direction=REVERSIBLE
