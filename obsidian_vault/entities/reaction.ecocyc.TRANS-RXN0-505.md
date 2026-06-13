---
entity_id: "reaction.ecocyc.TRANS-RXN0-505"
entity_type: "reaction"
name: "TRANS-RXN0-505"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-505"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-505

`reaction.ecocyc.TRANS-RXN0-505`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-505`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROPIONATE -> PROPIONATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROPIONATE -> PROPIONATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putP (protein.P07117). Substrates: Propanoate (molecule.C00163). Products: Propanoate (molecule.C00163).

## Annotation

PROPIONATE -> PROPIONATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07117|protein.P07117]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-505`

## Notes

PROPIONATE -> PROPIONATE; direction=LEFT-TO-RIGHT
