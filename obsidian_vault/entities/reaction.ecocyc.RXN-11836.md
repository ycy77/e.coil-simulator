---
entity_id: "reaction.ecocyc.RXN-11836"
entity_type: "reaction"
name: "RXN-11836"
source_database: "EcoCyc"
source_id: "RXN-11836"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11836

`reaction.ecocyc.RXN-11836`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11836`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23S-rRNA-uridine2605 -> 23S-rRNA-pseudouridine2605; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNA-uridine2605 -> 23S-rRNA-pseudouridine2605; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluB (protein.P37765). Substrates: uridine2605 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine2605). Products: a pseudouridine2605 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine2605).

## Annotation

23S-rRNA-uridine2605 -> 23S-rRNA-pseudouridine2605; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37765|protein.P37765]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine2605|molecule.ecocyc.23S-rRNA-pseudouridine2605]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine2605|molecule.ecocyc.23S-rRNA-uridine2605]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11836`

## Notes

23S-rRNA-uridine2605 -> 23S-rRNA-pseudouridine2605; direction=PHYSIOL-LEFT-TO-RIGHT
