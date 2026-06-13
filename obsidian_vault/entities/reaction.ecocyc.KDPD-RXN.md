---
entity_id: "reaction.ecocyc.KDPD-RXN"
entity_type: "reaction"
name: "KDPD-RXN"
source_database: "EcoCyc"
source_id: "KDPD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDPD-RXN

`reaction.ecocyc.KDPD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDPD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + KDPD-CPLX -> PHOSPHO-KDPD + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + KDPD-CPLX -> PHOSPHO-KDPD + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1495` KdpDE Two-Component Signal Transduction System, potassium-dependent (EcoCyc)

## Annotation

ATP + KDPD-CPLX -> PHOSPHO-KDPD + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1495` KdpDE Two-Component Signal Transduction System, potassium-dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[protein.P69829|protein.P69829]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:KDPD-RXN`

## Notes

ATP + KDPD-CPLX -> PHOSPHO-KDPD + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
