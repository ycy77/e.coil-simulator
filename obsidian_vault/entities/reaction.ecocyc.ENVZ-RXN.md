---
entity_id: "reaction.ecocyc.ENVZ-RXN"
entity_type: "reaction"
name: "ENVZ-RXN"
source_database: "EcoCyc"
source_id: "ENVZ-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENVZ-RXN

`reaction.ecocyc.ENVZ-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENVZ-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ENVZ-CPLX + ATP -> ADP + PHOSPHO-ENVZ; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ENVZ-CPLX + ATP -> ADP + PHOSPHO-ENVZ; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1500` EnvZ/OmpR Two-Component Signal Transduction System (EcoCyc)

## Annotation

ENVZ-CPLX + ATP -> ADP + PHOSPHO-ENVZ; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1500` EnvZ/OmpR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ENVZ-RXN`

## Notes

ENVZ-CPLX + ATP -> ADP + PHOSPHO-ENVZ; direction=PHYSIOL-LEFT-TO-RIGHT
