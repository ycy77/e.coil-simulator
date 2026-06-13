---
entity_id: "reaction.ecocyc.TRANS-RXN0-547"
entity_type: "reaction"
name: "passive diffusion of water"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-547"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG|CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# passive diffusion of water

`reaction.ecocyc.TRANS-RXN0-547`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-547`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG|CCO-OUTER-MEM

## Enriched Summary

Water can cross lipid bilayers by simple diffusion as represented in this reaction, by movement through water specific channels such as (CPLX0-7653 "AqpZ") or through the outer membrane porins. EcoCyc reaction equation: WATER -> WATER; direction=REVERSIBLE. Water can cross lipid bilayers by simple diffusion as represented in this reaction, by movement through water specific channels such as (CPLX0-7653 "AqpZ") or through the outer membrane porins.

## Biological Role

Substrates: H2O (molecule.C00001). Products: H2O (molecule.C00001).

## Annotation

Water can cross lipid bilayers by simple diffusion as represented in this reaction, by movement through water specific channels such as (CPLX0-7653 "AqpZ") or through the outer membrane porins.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-547`

## Notes

WATER -> WATER; direction=REVERSIBLE
