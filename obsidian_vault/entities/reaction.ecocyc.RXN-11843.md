---
entity_id: "reaction.ecocyc.RXN-11843"
entity_type: "reaction"
name: "RXN-11843"
source_database: "EcoCyc"
source_id: "RXN-11843"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11843

`reaction.ecocyc.RXN-11843`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11843`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23S-rRNA-uridine746 -> 23S-rRNA-pseudouridine746; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNA-uridine746 -> 23S-rRNA-pseudouridine746; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluA (protein.P0AA37). Substrates: uridine746 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine746). Products: a pseudouridine746 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine746).

## Annotation

23S-rRNA-uridine746 -> 23S-rRNA-pseudouridine746; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AA37|protein.P0AA37]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine746|molecule.ecocyc.23S-rRNA-pseudouridine746]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine746|molecule.ecocyc.23S-rRNA-uridine746]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11843`

## Notes

23S-rRNA-uridine746 -> 23S-rRNA-pseudouridine746; direction=LEFT-TO-RIGHT
