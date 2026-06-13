---
entity_id: "reaction.ecocyc.RXN-11835"
entity_type: "reaction"
name: "RXN-11835"
source_database: "EcoCyc"
source_id: "RXN-11835"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11835

`reaction.ecocyc.RXN-11835`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11835`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23S-rRNA-uridine2604 -> 23S-rRNA-pseudouridine2604; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNA-uridine2604 -> 23S-rRNA-pseudouridine2604; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluF (protein.P32684). Substrates: a uridine2604 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine2604). Products: a pseudouridine2604 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine2604).

## Annotation

23S-rRNA-uridine2604 -> 23S-rRNA-pseudouridine2604; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P32684|protein.P32684]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine2604|molecule.ecocyc.23S-rRNA-pseudouridine2604]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine2604|molecule.ecocyc.23S-rRNA-uridine2604]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11835`

## Notes

23S-rRNA-uridine2604 -> 23S-rRNA-pseudouridine2604; direction=PHYSIOL-LEFT-TO-RIGHT
