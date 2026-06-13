---
entity_id: "reaction.ecocyc.HYDH-RXN"
entity_type: "reaction"
name: "HYDH-RXN"
source_database: "EcoCyc"
source_id: "HYDH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HYDH-RXN

`reaction.ecocyc.HYDH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HYDH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

HYDH-MONOMER + ATP -> PHOSPHO-HYDH + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: HYDH-MONOMER + ATP -> PHOSPHO-HYDH + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1498` ZraSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

HYDH-MONOMER + ATP -> PHOSPHO-HYDH + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1498` ZraSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HYDH-RXN`

## Notes

HYDH-MONOMER + ATP -> PHOSPHO-HYDH + ADP; direction=LEFT-TO-RIGHT
