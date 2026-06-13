---
entity_id: "reaction.ecocyc.RXN0-5306"
entity_type: "reaction"
name: "RXN0-5306"
source_database: "EcoCyc"
source_id: "RXN0-5306"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5306

`reaction.ecocyc.RXN0-5306`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5306`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RHAMNOSE -> CPD0-1112; direction=LEFT-TO-RIGHT EcoCyc reaction equation: RHAMNOSE -> CPD0-1112; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-rhamnose mutarotase (complex.ecocyc.CPLX0-7649). Substrates: α-L-rhamnopyranose (molecule.ecocyc.RHAMNOSE). Products: β-L-rhamnopyranose (molecule.ecocyc.CPD0-1112).

## Enriched Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Annotation

RHAMNOSE -> CPD0-1112; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7649|complex.ecocyc.CPLX0-7649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1112|molecule.ecocyc.CPD0-1112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.RHAMNOSE__78fcd32f|molecule.ecocyc.RHAMNOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5306`

## Notes

RHAMNOSE -> CPD0-1112; direction=LEFT-TO-RIGHT
