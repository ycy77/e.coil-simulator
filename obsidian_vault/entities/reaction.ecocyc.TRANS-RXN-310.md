---
entity_id: "reaction.ecocyc.TRANS-RXN-310"
entity_type: "reaction"
name: "hydrogen sulfide diffusion"
source_database: "EcoCyc"
source_id: "TRANS-RXN-310"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hydrogen sulfide diffusion

`reaction.ecocyc.TRANS-RXN-310`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-310`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

HS -> HS; direction=REVERSIBLE EcoCyc reaction equation: HS -> HS; direction=REVERSIBLE.

## Biological Role

Substrates: Hydrogen sulfide (molecule.C00283). Products: Hydrogen sulfide (molecule.C00283).

## Annotation

HS -> HS; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-310`

## Notes

HS -> HS; direction=REVERSIBLE
