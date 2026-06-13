---
entity_id: "reaction.ecocyc.HISTOLDEHYD-RXN"
entity_type: "reaction"
name: "HISTOLDEHYD-RXN"
source_database: "EcoCyc"
source_id: "HISTOLDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HISTOLDEHYD-RXN

`reaction.ecocyc.HISTOLDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HISTOLDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the tenth step in the histidine biosynthesis pathway EcoCyc reaction equation: HISTIDINOL + NAD -> PROTON + HISTIDINAL + NADH; direction=REVERSIBLE. This is the tenth step in the histidine biosynthesis pathway

## Biological Role

Substrates: NAD+ (molecule.C00003), L-Histidinol (molecule.C00860). Products: NADH (molecule.C00004), H+ (molecule.C00080), L-Histidinal (molecule.C01929).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the tenth step in the histidine biosynthesis pathway

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01929|molecule.C01929]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00860|molecule.C00860]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HISTOLDEHYD-RXN`

## Notes

HISTIDINOL + NAD -> PROTON + HISTIDINAL + NADH; direction=REVERSIBLE
