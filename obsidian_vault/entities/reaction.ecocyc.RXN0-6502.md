---
entity_id: "reaction.ecocyc.RXN0-6502"
entity_type: "reaction"
name: "RXN0-6502"
source_database: "EcoCyc"
source_id: "RXN0-6502"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6502

`reaction.ecocyc.RXN0-6502`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6502`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + CPLX0-7870 -> PHOSPHO-ATOS + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPLX0-7870 -> PHOSPHO-ATOS + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1474` AtoSC Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + CPLX0-7870 -> PHOSPHO-ATOS + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1474` AtoSC Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00164|molecule.C00164]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `activates` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6502`

## Notes

ATP + CPLX0-7870 -> PHOSPHO-ATOS + ADP; direction=LEFT-TO-RIGHT
