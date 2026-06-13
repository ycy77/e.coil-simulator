---
entity_id: "reaction.ecocyc.RXN-11834"
entity_type: "reaction"
name: "RXN-11834"
source_database: "EcoCyc"
source_id: "RXN-11834"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11834

`reaction.ecocyc.RXN-11834`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11834`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23S-rRNA-uridine2457 -> 23S-rRNA-pseudouridine2457; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNA-uridine2457 -> 23S-rRNA-pseudouridine2457; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluE (protein.P75966). Substrates: uridine2457 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine2457). Products: a pseudouridine2457 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine2457).

## Annotation

23S-rRNA-uridine2457 -> 23S-rRNA-pseudouridine2457; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P75966|protein.P75966]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine2457|molecule.ecocyc.23S-rRNA-pseudouridine2457]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine2457|molecule.ecocyc.23S-rRNA-uridine2457]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11834`

## Notes

23S-rRNA-uridine2457 -> 23S-rRNA-pseudouridine2457; direction=PHYSIOL-LEFT-TO-RIGHT
