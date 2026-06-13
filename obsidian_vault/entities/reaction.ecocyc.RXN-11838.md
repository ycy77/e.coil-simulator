---
entity_id: "reaction.ecocyc.RXN-11838"
entity_type: "reaction"
name: "RXN-11838"
source_database: "EcoCyc"
source_id: "RXN-11838"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11838

`reaction.ecocyc.RXN-11838`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11838`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23S-rRNA-uridine955-2504-2580 -> 23S-rRNA-pseudouridine955-2504-2580; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNA-uridine955-2504-2580 -> 23S-rRNA-pseudouridine955-2504-2580; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluC (protein.P0AA39). Substrates: uridine955/2504/2580 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine955-2504-2580). Products: a pseudouridine955/2504/2580 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine955-2504-2580).

## Annotation

23S-rRNA-uridine955-2504-2580 -> 23S-rRNA-pseudouridine955-2504-2580; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AA39|protein.P0AA39]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine955-2504-2580|molecule.ecocyc.23S-rRNA-pseudouridine955-2504-2580]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine955-2504-2580|molecule.ecocyc.23S-rRNA-uridine955-2504-2580]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11838`

## Notes

23S-rRNA-uridine955-2504-2580 -> 23S-rRNA-pseudouridine955-2504-2580; direction=PHYSIOL-LEFT-TO-RIGHT
