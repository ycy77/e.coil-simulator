---
entity_id: "reaction.ecocyc.TRANS-RXN-69"
entity_type: "reaction"
name: "putrescine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-69"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# putrescine:proton symport

`reaction.ecocyc.TRANS-RXN-69`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-69`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + PUTRESCINE -> PROTON + PUTRESCINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + PUTRESCINE -> PROTON + PUTRESCINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by plaP (protein.P0AA47), potE (protein.P0AAF1), puuP (protein.P76037). Substrates: H+ (molecule.C00080), Putrescine (molecule.C00134). Products: H+ (molecule.C00080), Putrescine (molecule.C00134).

## Annotation

PROTON + PUTRESCINE -> PROTON + PUTRESCINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AA47|protein.P0AA47]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AAF1|protein.P0AAF1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76037|protein.P76037]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-69`

## Notes

PROTON + PUTRESCINE -> PROTON + PUTRESCINE; direction=REVERSIBLE
