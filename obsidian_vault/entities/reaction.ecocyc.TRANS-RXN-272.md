---
entity_id: "reaction.ecocyc.TRANS-RXN-272"
entity_type: "reaction"
name: "TRANS-RXN-272"
source_database: "EcoCyc"
source_id: "TRANS-RXN-272"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-272

`reaction.ecocyc.TRANS-RXN-272`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-272`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FAD -> FAD; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FAD -> FAD; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yeeO (protein.P76352). Substrates: FAD (molecule.C00016). Products: FAD (molecule.C00016).

## Annotation

FAD -> FAD; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76352|protein.P76352]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-272`

## Notes

FAD -> FAD; direction=LEFT-TO-RIGHT
