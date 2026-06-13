---
entity_id: "reaction.ecocyc.BASS-RXN"
entity_type: "reaction"
name: "BASS-RXN"
source_database: "EcoCyc"
source_id: "BASS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BASS-RXN

`reaction.ecocyc.BASS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BASS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + BASS-MONOMER -> ADP + PHOSPHO-BASS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + BASS-MONOMER -> ADP + PHOSPHO-BASS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1482` BasSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + BASS-MONOMER -> ADP + PHOSPHO-BASS; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1482` BasSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BASS-RXN`

## Notes

ATP + BASS-MONOMER -> ADP + PHOSPHO-BASS; direction=PHYSIOL-LEFT-TO-RIGHT
