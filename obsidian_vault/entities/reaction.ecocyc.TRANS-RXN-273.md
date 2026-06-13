---
entity_id: "reaction.ecocyc.TRANS-RXN-273"
entity_type: "reaction"
name: "TRANS-RXN-273"
source_database: "EcoCyc"
source_id: "TRANS-RXN-273"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-273

`reaction.ecocyc.TRANS-RXN-273`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-273`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-14545 -> CPD-14545; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14545 -> CPD-14545; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nimT (protein.P76242). Substrates: 2-nitroimidazole (molecule.ecocyc.CPD-14545). Products: 2-nitroimidazole (molecule.ecocyc.CPD-14545).

## Annotation

CPD-14545 -> CPD-14545; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76242|protein.P76242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-14545|molecule.ecocyc.CPD-14545]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-14545|molecule.ecocyc.CPD-14545]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-273`

## Notes

CPD-14545 -> CPD-14545; direction=LEFT-TO-RIGHT
