---
entity_id: "reaction.ecocyc.RXN0-1802"
entity_type: "reaction"
name: "RXN0-1802"
source_database: "EcoCyc"
source_id: "RXN0-1802"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1802

`reaction.ecocyc.RXN0-1802`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1802`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Long-Chain-Fatty-Acids -> Long-Chain-Fatty-Acids; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Long-Chain-Fatty-Acids -> Long-Chain-Fatty-Acids; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fadL (protein.P10384). Substrates: Long-chain fatty acid (molecule.C00638). Products: Long-chain fatty acid (molecule.C00638).

## Annotation

Long-Chain-Fatty-Acids -> Long-Chain-Fatty-Acids; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P10384|protein.P10384]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00638|molecule.C00638]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00638|molecule.C00638]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1802`

## Notes

Long-Chain-Fatty-Acids -> Long-Chain-Fatty-Acids; direction=LEFT-TO-RIGHT
