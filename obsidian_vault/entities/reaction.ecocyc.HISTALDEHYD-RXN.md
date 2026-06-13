---
entity_id: "reaction.ecocyc.HISTALDEHYD-RXN"
entity_type: "reaction"
name: "HISTALDEHYD-RXN"
source_database: "EcoCyc"
source_id: "HISTALDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HISTALDEHYD-RXN

`reaction.ecocyc.HISTALDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HISTALDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the eleventh step in the histidine biosynthesis pathway EcoCyc reaction equation: HISTIDINAL + NAD + WATER -> PROTON + HIS + NADH; direction=PHYSIOL-LEFT-TO-RIGHT. This is the eleventh step in the histidine biosynthesis pathway

## Biological Role

Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), L-Histidinal (molecule.C01929). Products: NADH (molecule.C00004), H+ (molecule.C00080), L-Histidine (molecule.C00135).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the eleventh step in the histidine biosynthesis pathway

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01929|molecule.C01929]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HISTALDEHYD-RXN`

## Notes

HISTIDINAL + NAD + WATER -> PROTON + HIS + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
