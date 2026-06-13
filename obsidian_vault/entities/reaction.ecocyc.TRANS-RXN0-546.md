---
entity_id: "reaction.ecocyc.TRANS-RXN0-546"
entity_type: "reaction"
name: "ethanol diffusion"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-546"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ethanol diffusion

`reaction.ecocyc.TRANS-RXN0-546`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-546`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Pure phospholipid artificial membranes are permeable to ethanol . EcoCyc reaction equation: ETOH -> ETOH; direction=REVERSIBLE. Pure phospholipid artificial membranes are permeable to ethanol .

## Biological Role

Substrates: Ethanol (molecule.C00469). Products: Ethanol (molecule.C00469).

## Annotation

Pure phospholipid artificial membranes are permeable to ethanol .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00469|molecule.C00469]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00469|molecule.C00469]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-546`

## Notes

ETOH -> ETOH; direction=REVERSIBLE
