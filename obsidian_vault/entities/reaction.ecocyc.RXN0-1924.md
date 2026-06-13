---
entity_id: "reaction.ecocyc.RXN0-1924"
entity_type: "reaction"
name: "L-cysteine export"
source_database: "EcoCyc"
source_id: "RXN0-1924"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-cysteine export

`reaction.ecocyc.RXN0-1924`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1924`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CYS -> CYS; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CYS -> CYS; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by eamA (protein.P31125), eamB (protein.P38101). Substrates: L-Cysteine (molecule.C00097). Products: L-Cysteine (molecule.C00097).

## Annotation

CYS -> CYS; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P31125|protein.P31125]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P38101|protein.P38101]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1924`

## Notes

CYS -> CYS; direction=LEFT-TO-RIGHT
