---
entity_id: "reaction.ecocyc.RXN-11833"
entity_type: "reaction"
name: "RXN-11833"
source_database: "EcoCyc"
source_id: "RXN-11833"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11833

`reaction.ecocyc.RXN-11833`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11833`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

16S-rRNA-uridine516 -> 16S-rRNA-pseudouridine516; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 16S-rRNA-uridine516 -> 16S-rRNA-pseudouridine516; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rsuA (protein.P0AA43). Substrates: a uridine516 in 16S rRNA (molecule.ecocyc.16S-rRNA-uridine516). Products: a 16S rRNA pseudouridine516 (molecule.ecocyc.16S-rRNA-pseudouridine516).

## Annotation

16S-rRNA-uridine516 -> 16S-rRNA-pseudouridine516; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AA43|protein.P0AA43]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-pseudouridine516|molecule.ecocyc.16S-rRNA-pseudouridine516]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-uridine516|molecule.ecocyc.16S-rRNA-uridine516]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11833`

## Notes

16S-rRNA-uridine516 -> 16S-rRNA-pseudouridine516; direction=LEFT-TO-RIGHT
