---
entity_id: "reaction.ecocyc.TRANS-RXN0-211"
entity_type: "reaction"
name: "putrescine:ornithine antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-211"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# putrescine:ornithine antiport

`reaction.ecocyc.TRANS-RXN0-211`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-211`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PUTRESCINE + L-ORNITHINE -> PUTRESCINE + L-ORNITHINE; direction=REVERSIBLE EcoCyc reaction equation: PUTRESCINE + L-ORNITHINE -> PUTRESCINE + L-ORNITHINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by potE (protein.P0AAF1). Substrates: L-Ornithine (molecule.C00077), Putrescine (molecule.C00134). Products: L-Ornithine (molecule.C00077), Putrescine (molecule.C00134).

## Annotation

PUTRESCINE + L-ORNITHINE -> PUTRESCINE + L-ORNITHINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAF1|protein.P0AAF1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-211`

## Notes

PUTRESCINE + L-ORNITHINE -> PUTRESCINE + L-ORNITHINE; direction=REVERSIBLE
