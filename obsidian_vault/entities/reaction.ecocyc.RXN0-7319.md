---
entity_id: "reaction.ecocyc.RXN0-7319"
entity_type: "reaction"
name: "RXN0-7319"
source_database: "EcoCyc"
source_id: "RXN0-7319"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7319

`reaction.ecocyc.RXN0-7319`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7319`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-381 + ETR-Quinones -> 2-KETOGLUTARATE + ETR-Quinols; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-381 + ETR-Quinones -> 2-KETOGLUTARATE + ETR-Quinols; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lhgD (protein.P37339). Substrates: (S)-2-Hydroxyglutarate (molecule.C03196). Products: 2-Oxoglutarate (molecule.C00026).

## Enriched Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

CPD-381 + ETR-Quinones -> 2-KETOGLUTARATE + ETR-Quinols; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37339|protein.P37339]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03196|molecule.C03196]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7319`

## Notes

CPD-381 + ETR-Quinones -> 2-KETOGLUTARATE + ETR-Quinols; direction=LEFT-TO-RIGHT
