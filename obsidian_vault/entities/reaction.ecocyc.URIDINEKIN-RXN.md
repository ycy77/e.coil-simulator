---
entity_id: "reaction.ecocyc.URIDINEKIN-RXN"
entity_type: "reaction"
name: "URIDINEKIN-RXN"
source_database: "EcoCyc"
source_id: "URIDINEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URIDINEKIN-RXN

`reaction.ecocyc.URIDINEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URIDINEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

URIDINE + ATP -> PROTON + UMP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: URIDINE + ATP -> PROTON + UMP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by udk (protein.P0A8F4). Substrates: ATP (molecule.C00002), Uridine (molecule.C00299). Products: ADP (molecule.C00008), H+ (molecule.C00080), UMP (molecule.C00105).

## Enriched Pathways

- `ecocyc.PWY-7193` pyrimidine ribonucleosides salvage I (EcoCyc)

## Annotation

URIDINE + ATP -> PROTON + UMP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7193` pyrimidine ribonucleosides salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A8F4|protein.P0A8F4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:URIDINEKIN-RXN`

## Notes

URIDINE + ATP -> PROTON + UMP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
