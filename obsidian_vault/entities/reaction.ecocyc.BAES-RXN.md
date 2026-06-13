---
entity_id: "reaction.ecocyc.BAES-RXN"
entity_type: "reaction"
name: "BAES-RXN"
source_database: "EcoCyc"
source_id: "BAES-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BAES-RXN

`reaction.ecocyc.BAES-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BAES-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

BAES-MONOMER + ATP -> PHOSPHO-BAES + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: BAES-MONOMER + ATP -> PHOSPHO-BAES + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1481` BaeSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

BAES-MONOMER + ATP -> PHOSPHO-BAES + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1481` BaeSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BAES-RXN`

## Notes

BAES-MONOMER + ATP -> PHOSPHO-BAES + ADP; direction=LEFT-TO-RIGHT
