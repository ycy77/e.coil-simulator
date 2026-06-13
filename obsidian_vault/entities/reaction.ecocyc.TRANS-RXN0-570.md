---
entity_id: "reaction.ecocyc.TRANS-RXN0-570"
entity_type: "reaction"
name: "pyruvate export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-570"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# pyruvate export

`reaction.ecocyc.TRANS-RXN0-570`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-570`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Direct transport tests and genetic analysis of mutants unable to transport pyruvate suggests that E. coli K-12 contains both inducible and constitutive transport systems for the import of pyruvate plus an additional system for pyruvate efflux . EcoCyc reaction equation: PYRUVATE -> PYRUVATE; direction=LEFT-TO-RIGHT. Direct transport tests and genetic analysis of mutants unable to transport pyruvate suggests that E. coli K-12 contains both inducible and constitutive transport systems for the import of pyruvate plus an additional system for pyruvate efflux .

## Biological Role

Substrates: Pyruvate (molecule.C00022). Products: Pyruvate (molecule.C00022).

## Annotation

Direct transport tests and genetic analysis of mutants unable to transport pyruvate suggests that E. coli K-12 contains both inducible and constitutive transport systems for the import of pyruvate plus an additional system for pyruvate efflux .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-570`

## Notes

PYRUVATE -> PYRUVATE; direction=LEFT-TO-RIGHT
