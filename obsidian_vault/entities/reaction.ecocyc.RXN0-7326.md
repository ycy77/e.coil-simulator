---
entity_id: "reaction.ecocyc.RXN0-7326"
entity_type: "reaction"
name: "RXN0-7326"
source_database: "EcoCyc"
source_id: "RXN0-7326"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7326

`reaction.ecocyc.RXN0-7326`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7326`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + CPLX0-10815 -> MONOMER0-4457 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPLX0-10815 -> MONOMER0-4457 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1559` BtsSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + CPLX0-10815 -> MONOMER0-4457 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1559` BtsSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7326`

## Notes

ATP + CPLX0-10815 -> MONOMER0-4457 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
