---
entity_id: "reaction.ecocyc.2.3.1.49-RXN"
entity_type: "reaction"
name: "2.3.1.49-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.49-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.3.1.49-RXN

`reaction.ecocyc.2.3.1.49-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.49-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HOLO-CITRATE-LYASE + S-ACETYLPHOSPHOPANTETHEINE -> CITRATE-LYASE + PANTETHEINE-P; direction=LEFT-TO-RIGHT EcoCyc reaction equation: HOLO-CITRATE-LYASE + S-ACETYLPHOSPHOPANTETHEINE -> CITRATE-LYASE + PANTETHEINE-P; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: S-acetyl phosphopantetheine (molecule.ecocyc.S-ACETYLPHOSPHOPANTETHEINE). Products: Pantetheine 4'-phosphate (molecule.C01134).

## Enriched Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Annotation

HOLO-CITRATE-LYASE + S-ACETYLPHOSPHOPANTETHEINE -> CITRATE-LYASE + PANTETHEINE-P; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C01134|molecule.C01134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.S-ACETYLPHOSPHOPANTETHEINE|molecule.ecocyc.S-ACETYLPHOSPHOPANTETHEINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.3.1.49-RXN`

## Notes

HOLO-CITRATE-LYASE + S-ACETYLPHOSPHOPANTETHEINE -> CITRATE-LYASE + PANTETHEINE-P; direction=LEFT-TO-RIGHT
