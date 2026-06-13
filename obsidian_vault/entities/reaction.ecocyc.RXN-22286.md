---
entity_id: "reaction.ecocyc.RXN-22286"
entity_type: "reaction"
name: "RXN-22286"
source_database: "EcoCyc"
source_id: "RXN-22286"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22286

`reaction.ecocyc.RXN-22286`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22286`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-846 + PROTON -> HS; direction=REVERSIBLE EcoCyc reaction equation: CPD-846 + PROTON -> HS; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), hydrosulfide (molecule.ecocyc.CPD-846). Products: Hydrogen sulfide (molecule.C00283).

## Annotation

CPD-846 + PROTON -> HS; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-846|molecule.ecocyc.CPD-846]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22286`

## Notes

CPD-846 + PROTON -> HS; direction=REVERSIBLE
