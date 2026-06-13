---
entity_id: "reaction.ecocyc.TRANS-RXN-1"
entity_type: "reaction"
name: "TRANS-RXN-1"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-1

`reaction.ecocyc.TRANS-RXN-1`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FORMATE -> FORMATE; direction=REVERSIBLE EcoCyc reaction equation: FORMATE -> FORMATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by formate channel FocA (complex.ecocyc.CPLX0-7843), focB (protein.P77733). Substrates: Formate (molecule.C00058). Products: Formate (molecule.C00058).

## Annotation

FORMATE -> FORMATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7843|complex.ecocyc.CPLX0-7843]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77733|protein.P77733]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-1`

## Notes

FORMATE -> FORMATE; direction=REVERSIBLE
