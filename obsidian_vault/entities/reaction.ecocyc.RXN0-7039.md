---
entity_id: "reaction.ecocyc.RXN0-7039"
entity_type: "reaction"
name: "RXN0-7039"
source_database: "EcoCyc"
source_id: "RXN0-7039"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7039

`reaction.ecocyc.RXN0-7039`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7039`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

G7243-MONOMER + ATP -> MONOMER0-4287 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: G7243-MONOMER + ATP -> MONOMER0-4287 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1550` PyrSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

G7243-MONOMER + ATP -> MONOMER0-4287 + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1550` PyrSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7039`

## Notes

G7243-MONOMER + ATP -> MONOMER0-4287 + ADP; direction=LEFT-TO-RIGHT
