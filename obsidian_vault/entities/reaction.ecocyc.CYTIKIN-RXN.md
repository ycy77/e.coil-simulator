---
entity_id: "reaction.ecocyc.CYTIKIN-RXN"
entity_type: "reaction"
name: "CYTIKIN-RXN"
source_database: "EcoCyc"
source_id: "CYTIKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYTIKIN-RXN

`reaction.ecocyc.CYTIKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYTIKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYTIDINE + ATP -> CMP + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYTIDINE + ATP -> CMP + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by udk (protein.P0A8F4). Substrates: ATP (molecule.C00002), Cytidine (molecule.C00475). Products: ADP (molecule.C00008), CMP (molecule.C00055), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-7193` pyrimidine ribonucleosides salvage I (EcoCyc)

## Annotation

CYTIDINE + ATP -> CMP + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7193` pyrimidine ribonucleosides salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A8F4|protein.P0A8F4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CYTIKIN-RXN`

## Notes

CYTIDINE + ATP -> CMP + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
