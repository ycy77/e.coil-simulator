---
entity_id: "reaction.ecocyc.RXN0-7433"
entity_type: "reaction"
name: "RXN0-7433"
source_database: "EcoCyc"
source_id: "RXN0-7433"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7433

`reaction.ecocyc.RXN0-7433`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7433`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by proXp-y (protein.P64483). Substrates: H2O (molecule.C00001). Products: L-Serine (molecule.C00065), H+ (molecule.C00080).

## Annotation

Seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P64483|protein.P64483]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7433`

## Notes

Seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
