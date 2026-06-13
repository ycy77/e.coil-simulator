---
entity_id: "reaction.ecocyc.TRANS-RXN0-453"
entity_type: "reaction"
name: "TRANS-RXN0-453"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-453"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-453

`reaction.ecocyc.TRANS-RXN0-453`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-453`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-10774 -> CPD-10774; direction=REVERSIBLE EcoCyc reaction equation: CPD-10774 -> CPD-10774; direction=REVERSIBLE.

## Biological Role

Catalyzed by tqsA (protein.P0AFS5). Substrates: R-THMF (molecule.C21382). Products: R-THMF (molecule.C21382).

## Annotation

CPD-10774 -> CPD-10774; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AFS5|protein.P0AFS5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C21382|molecule.C21382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C21382|molecule.C21382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-453`

## Notes

CPD-10774 -> CPD-10774; direction=REVERSIBLE
