---
entity_id: "reaction.ecocyc.PHOQ-RXN"
entity_type: "reaction"
name: "PHOQ-RXN"
source_database: "EcoCyc"
source_id: "PHOQ-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOQ-RXN

`reaction.ecocyc.PHOQ-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOQ-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPLX0-8168 + ATP -> PHOSPHO-PHOQ + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPLX0-8168 + ATP -> PHOSPHO-PHOQ + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1458` PhoQP Two-Component Signal Transduction System, magnesium-dependent (EcoCyc)

## Annotation

CPLX0-8168 + ATP -> PHOSPHO-PHOQ + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1458` PhoQP Two-Component Signal Transduction System, magnesium-dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions

## External IDs

- `EcoCyc:PHOQ-RXN`

## Notes

CPLX0-8168 + ATP -> PHOSPHO-PHOQ + ADP; direction=LEFT-TO-RIGHT
