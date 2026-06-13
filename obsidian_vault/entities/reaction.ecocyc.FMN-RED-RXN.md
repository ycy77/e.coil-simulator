---
entity_id: "reaction.ecocyc.FMN-RED-RXN"
entity_type: "reaction"
name: "FMN-RED-RXN"
source_database: "EcoCyc"
source_id: "FMN-RED-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FMN-RED-RXN

`reaction.ecocyc.FMN-RED-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FMN-RED-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADH-P-OR-NOP + Ox-FMN-Flavoproteins + PROTON -> NAD-P-OR-NOP + Red-FMNH2-Flavoproteins; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NADH-P-OR-NOP + Ox-FMN-Flavoproteins + PROTON -> NAD-P-OR-NOP + Red-FMNH2-Flavoproteins; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

NADH-P-OR-NOP + Ox-FMN-Flavoproteins + PROTON -> NAD-P-OR-NOP + Red-FMNH2-Flavoproteins; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FMN-RED-RXN`

## Notes

NADH-P-OR-NOP + Ox-FMN-Flavoproteins + PROTON -> NAD-P-OR-NOP + Red-FMNH2-Flavoproteins; direction=LEFT-TO-RIGHT
