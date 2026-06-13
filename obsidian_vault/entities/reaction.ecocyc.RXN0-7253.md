---
entity_id: "reaction.ecocyc.RXN0-7253"
entity_type: "reaction"
name: "RXN0-7253"
source_database: "EcoCyc"
source_id: "RXN0-7253"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7253

`reaction.ecocyc.RXN0-7253`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7253`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-uridine35 -> tRNA-pseudouridine35; direction=LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-uridine35 -> tRNA-pseudouridine35; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluF (protein.P32684). Substrates: a uridine35 in tRNA (molecule.ecocyc.tRNA-uridine35). Products: a pseudouridine35 in tRNA (molecule.ecocyc.tRNA-pseudouridine35).

## Annotation

tRNA-uridine35 -> tRNA-pseudouridine35; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P32684|protein.P32684]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNA-pseudouridine35|molecule.ecocyc.tRNA-pseudouridine35]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine35|molecule.ecocyc.tRNA-uridine35]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7253`

## Notes

tRNA-uridine35 -> tRNA-pseudouridine35; direction=LEFT-TO-RIGHT
