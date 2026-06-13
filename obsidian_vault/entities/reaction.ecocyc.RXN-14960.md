---
entity_id: "reaction.ecocyc.RXN-14960"
entity_type: "reaction"
name: "RXN-14960"
source_database: "EcoCyc"
source_id: "RXN-14960"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14960

`reaction.ecocyc.RXN-14960`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14960`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Fe2-siderophores + PROTON -> Siderophore + FE+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Fe2-siderophores + PROTON -> Siderophore + FE+2; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a siderophore-bound Fe(II) (molecule.ecocyc.Fe2-siderophores). Products: Fe2+ (molecule.C14818), a siderophore (molecule.ecocyc.Siderophore).

## Annotation

Fe2-siderophores + PROTON -> Siderophore + FE+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Siderophore|molecule.ecocyc.Siderophore]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Fe2-siderophores|molecule.ecocyc.Fe2-siderophores]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14960`

## Notes

Fe2-siderophores + PROTON -> Siderophore + FE+2; direction=LEFT-TO-RIGHT
