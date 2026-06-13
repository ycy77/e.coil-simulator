---
entity_id: "reaction.ecocyc.RXN0-5298"
entity_type: "reaction"
name: "RXN0-5298"
source_database: "EcoCyc"
source_id: "RXN0-5298"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5298

`reaction.ecocyc.RXN0-5298`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5298`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10329 -> CPD0-1107; direction=REVERSIBLE EcoCyc reaction equation: CPD-10329 -> CPD0-1107; direction=REVERSIBLE.

## Biological Role

Catalyzed by L-fucose mutarotase (complex.ecocyc.CPLX0-7645). Substrates: alpha-L-Fucopyranose (molecule.C20835). Products: beta-L-Fucopyranose (molecule.C20836).

## Enriched Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Annotation

CPD-10329 -> CPD0-1107; direction=REVERSIBLE

## Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7645|complex.ecocyc.CPLX0-7645]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C20836|molecule.C20836]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20835|molecule.C20835]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5298`

## Notes

CPD-10329 -> CPD0-1107; direction=REVERSIBLE
