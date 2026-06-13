---
entity_id: "reaction.ecocyc.RXN-23966"
entity_type: "reaction"
name: "L-cysteine import"
source_database: "EcoCyc"
source_id: "RXN-23966"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-cysteine import

`reaction.ecocyc.RXN-23966`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23966`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CYS -> CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS -> CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dlsT (protein.P42628). Substrates: L-Cysteine (molecule.C00097). Products: L-Cysteine (molecule.C00097).

## Annotation

CYS -> CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P42628|protein.P42628]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23966`

## Notes

CYS -> CYS; direction=PHYSIOL-LEFT-TO-RIGHT
