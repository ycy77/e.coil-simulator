---
entity_id: "reaction.ecocyc.TRANS-RXN0-556"
entity_type: "reaction"
name: "diffusion of carbon monoxide"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-556"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG|CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# diffusion of carbon monoxide

`reaction.ecocyc.TRANS-RXN0-556`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-556`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG|CCO-OUTER-MEM

## Enriched Summary

CARBON-MONOXIDE -> CARBON-MONOXIDE; direction=REVERSIBLE EcoCyc reaction equation: CARBON-MONOXIDE -> CARBON-MONOXIDE; direction=REVERSIBLE.

## Biological Role

Substrates: CO (molecule.C00237). Products: CO (molecule.C00237).

## Annotation

CARBON-MONOXIDE -> CARBON-MONOXIDE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-556`

## Notes

CARBON-MONOXIDE -> CARBON-MONOXIDE; direction=REVERSIBLE
