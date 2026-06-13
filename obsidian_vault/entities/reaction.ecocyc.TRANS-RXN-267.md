---
entity_id: "reaction.ecocyc.TRANS-RXN-267"
entity_type: "reaction"
name: "transport of cystine"
source_database: "EcoCyc"
source_id: "TRANS-RXN-267"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# transport of cystine

`reaction.ecocyc.TRANS-RXN-267`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-267`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

cystine -> cystine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: cystine -> cystine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yijE (protein.P0ABT8). Substrates: cystine (molecule.ecocyc.cystine). Products: cystine (molecule.ecocyc.cystine).

## Annotation

cystine -> cystine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0ABT8|protein.P0ABT8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.cystine|molecule.ecocyc.cystine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.cystine|molecule.ecocyc.cystine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-267`

## Notes

cystine -> cystine; direction=LEFT-TO-RIGHT
