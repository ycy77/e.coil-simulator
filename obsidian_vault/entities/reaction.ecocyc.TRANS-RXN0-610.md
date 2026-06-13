---
entity_id: "reaction.ecocyc.TRANS-RXN0-610"
entity_type: "reaction"
name: "diffusion of H2"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-610"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM|CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# diffusion of H2

`reaction.ecocyc.TRANS-RXN0-610`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-610`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM|CCO-PM-BAC-NEG

## Enriched Summary

HYDROGEN-MOLECULE -> HYDROGEN-MOLECULE; direction=REVERSIBLE EcoCyc reaction equation: HYDROGEN-MOLECULE -> HYDROGEN-MOLECULE; direction=REVERSIBLE.

## Biological Role

Substrates: Hydrogen (molecule.C00282). Products: Hydrogen (molecule.C00282).

## Annotation

HYDROGEN-MOLECULE -> HYDROGEN-MOLECULE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-610`

## Notes

HYDROGEN-MOLECULE -> HYDROGEN-MOLECULE; direction=REVERSIBLE
