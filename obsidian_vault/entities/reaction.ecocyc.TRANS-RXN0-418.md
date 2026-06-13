---
entity_id: "reaction.ecocyc.TRANS-RXN0-418"
entity_type: "reaction"
name: "TRANS-RXN0-418"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-418"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-418

`reaction.ecocyc.TRANS-RXN0-418`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-418`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PSICOSELYSINE -> PSICOSELYSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PSICOSELYSINE -> PSICOSELYSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by frlA (protein.P45539). Substrates: N6-(D-psicosyl)-L-lysine (molecule.ecocyc.PSICOSELYSINE). Products: N6-(D-psicosyl)-L-lysine (molecule.ecocyc.PSICOSELYSINE).

## Annotation

PSICOSELYSINE -> PSICOSELYSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P45539|protein.P45539]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.PSICOSELYSINE|molecule.ecocyc.PSICOSELYSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.PSICOSELYSINE|molecule.ecocyc.PSICOSELYSINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-418`

## Notes

PSICOSELYSINE -> PSICOSELYSINE; direction=LEFT-TO-RIGHT
