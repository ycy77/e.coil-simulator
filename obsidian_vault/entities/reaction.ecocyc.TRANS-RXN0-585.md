---
entity_id: "reaction.ecocyc.TRANS-RXN0-585"
entity_type: "reaction"
name: "Co2+ export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-585"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Co2+ export

`reaction.ecocyc.TRANS-RXN0-585`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-585`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CO+2 -> CO+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CO+2 -> CO+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rcnA (protein.P76425). Substrates: Cobalt ion (molecule.C00175). Products: Cobalt ion (molecule.C00175).

## Annotation

CO+2 -> CO+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76425|protein.P76425]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-585`

## Notes

CO+2 -> CO+2; direction=LEFT-TO-RIGHT
