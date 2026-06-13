---
entity_id: "reaction.ecocyc.RXN0-5285"
entity_type: "reaction"
name: "RXN0-5285"
source_database: "EcoCyc"
source_id: "RXN0-5285"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5285

`reaction.ecocyc.RXN0-5285`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5285`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1090 -> D-GLUCARATE; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1090 -> D-GLUCARATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by gudD (protein.P0AES2). Substrates: L-idarate (molecule.ecocyc.CPD0-1090). Products: D-Glucarate (molecule.C00818).

## Annotation

CPD0-1090 -> D-GLUCARATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AES2|protein.P0AES2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00818|molecule.C00818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1090|molecule.ecocyc.CPD0-1090]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5285`

## Notes

CPD0-1090 -> D-GLUCARATE; direction=REVERSIBLE
