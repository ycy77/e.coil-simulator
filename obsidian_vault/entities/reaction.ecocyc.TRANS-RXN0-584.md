---
entity_id: "reaction.ecocyc.TRANS-RXN0-584"
entity_type: "reaction"
name: "Ni2+ export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-584"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Ni2+ export

`reaction.ecocyc.TRANS-RXN0-584`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-584`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NI+2 -> NI+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NI+2 -> NI+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rcnA (protein.P76425). Substrates: Nickel(2+) (molecule.C19609). Products: Nickel(2+) (molecule.C19609).

## Annotation

NI+2 -> NI+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76425|protein.P76425]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-584`

## Notes

NI+2 -> NI+2; direction=LEFT-TO-RIGHT
