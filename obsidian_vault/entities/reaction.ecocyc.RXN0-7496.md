---
entity_id: "reaction.ecocyc.RXN0-7496"
entity_type: "reaction"
name: "RXN0-7496"
source_database: "EcoCyc"
source_id: "RXN0-7496"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7496

`reaction.ecocyc.RXN0-7496`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7496`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-DNA-Holliday-junction + WATER -> nicked-duplex-DNA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-DNA-Holliday-junction + WATER -> nicked-duplex-DNA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ruvC (protein.P0A814). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080).

## Annotation

a-DNA-Holliday-junction + WATER -> nicked-duplex-DNA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A814|protein.P0A814]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7496`

## Notes

a-DNA-Holliday-junction + WATER -> nicked-duplex-DNA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
