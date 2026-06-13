---
entity_id: "reaction.ecocyc.FCLEPIM-RXN"
entity_type: "reaction"
name: "FCLEPIM-RXN"
source_database: "EcoCyc"
source_id: "FCLEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FCLEPIM-RXN

`reaction.ecocyc.FCLEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FCLEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: GDP-4-dehydro-6-deoxy-D-mannose (molecule.C01222). Products: GDP-4-dehydro-6-deoxy-β-L-galactose (molecule.ecocyc.GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE).

## Enriched Pathways

- `ecocyc.PWY-66` GDP-L-fucose biosynthesis I (from GDP-D-mannose) (EcoCyc)

## Annotation

GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-66` GDP-L-fucose biosynthesis I (from GDP-D-mannose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE|molecule.ecocyc.GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01222|molecule.C01222]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FCLEPIM-RXN`

## Notes

GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE; direction=PHYSIOL-LEFT-TO-RIGHT
