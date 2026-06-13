---
entity_id: "reaction.ecocyc.TRANS-RXN0-417"
entity_type: "reaction"
name: "TRANS-RXN0-417"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-417"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-417

`reaction.ecocyc.TRANS-RXN0-417`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-417`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FRUCTOSELYSINE -> FRUCTOSELYSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FRUCTOSELYSINE -> FRUCTOSELYSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by frlA (protein.P45539). Substrates: Fructoselysine (molecule.C16488). Products: Fructoselysine (molecule.C16488).

## Annotation

FRUCTOSELYSINE -> FRUCTOSELYSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P45539|protein.P45539]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C16488|molecule.C16488]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16488|molecule.C16488]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-417`

## Notes

FRUCTOSELYSINE -> FRUCTOSELYSINE; direction=LEFT-TO-RIGHT
