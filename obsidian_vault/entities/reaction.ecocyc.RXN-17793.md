---
entity_id: "reaction.ecocyc.RXN-17793"
entity_type: "reaction"
name: "RXN-17793"
source_database: "EcoCyc"
source_id: "RXN-17793"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17793

`reaction.ecocyc.RXN-17793`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17793`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19154 -> CPD-19161 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-19154 -> CPD-19161 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: (S)-3-hydroxy-(7Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-19154). Products: H2O (molecule.C00001), (2E,7Z)-tetradec-2,7-enoyl-CoA (molecule.ecocyc.CPD-19161).

## Annotation

CPD-19154 -> CPD-19161 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19161|molecule.ecocyc.CPD-19161]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19154|molecule.ecocyc.CPD-19154]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17793`

## Notes

CPD-19154 -> CPD-19161 + WATER; direction=REVERSIBLE
