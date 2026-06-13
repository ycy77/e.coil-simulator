---
entity_id: "reaction.ecocyc.RXN0-7227"
entity_type: "reaction"
name: "RXN0-7227"
source_database: "EcoCyc"
source_id: "RXN0-7227"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7227

`reaction.ecocyc.RXN0-7227`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7227`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETR-Quinones + CPD-3564 -> ETR-Quinols + 2-OXOBUTANOATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ETR-Quinones + CPD-3564 -> ETR-Quinols + 2-OXOBUTANOATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lldD (protein.P33232). Substrates: 2-Hydroxybutanoic acid (molecule.C05984). Products: 2-Oxobutanoate (molecule.C00109).

## Annotation

ETR-Quinones + CPD-3564 -> ETR-Quinols + 2-OXOBUTANOATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P33232|protein.P33232]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05984|molecule.C05984]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7227`

## Notes

ETR-Quinones + CPD-3564 -> ETR-Quinols + 2-OXOBUTANOATE; direction=PHYSIOL-LEFT-TO-RIGHT
