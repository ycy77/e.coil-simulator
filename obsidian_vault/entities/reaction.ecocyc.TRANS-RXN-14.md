---
entity_id: "reaction.ecocyc.TRANS-RXN-14"
entity_type: "reaction"
name: "TRANS-RXN-14"
source_database: "EcoCyc"
source_id: "TRANS-RXN-14"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-14

`reaction.ecocyc.TRANS-RXN-14`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-14`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-69 -> CPD-69; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-69 -> CPD-69; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cynX (protein.P17583). Substrates: Cyanate (molecule.C01417). Products: Cyanate (molecule.C01417).

## Annotation

CPD-69 -> CPD-69; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P17583|protein.P17583]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-14`

## Notes

CPD-69 -> CPD-69; direction=LEFT-TO-RIGHT
