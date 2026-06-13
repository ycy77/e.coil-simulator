---
entity_id: "reaction.ecocyc.RXN0-7105"
entity_type: "reaction"
name: "RXN0-7105"
source_database: "EcoCyc"
source_id: "RXN0-7105"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7105

`reaction.ecocyc.RXN0-7105`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7105`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPLX0-7849 + WATER -> ENTB-CPLX + 2-3-DIHYDROXYBENZOATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPLX0-7849 + WATER -> ENTB-CPLX + 2-3-DIHYDROXYBENZOATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by proofreading thioesterase in enterobactin biosynthesis (complex.ecocyc.CPLX0-7766). Substrates: H2O (molecule.C00001). Products: 2,3-Dihydroxybenzoate (molecule.C00196).

## Annotation

CPLX0-7849 + WATER -> ENTB-CPLX + 2-3-DIHYDROXYBENZOATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7766|complex.ecocyc.CPLX0-7766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00196|molecule.C00196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7105`

## Notes

CPLX0-7849 + WATER -> ENTB-CPLX + 2-3-DIHYDROXYBENZOATE; direction=LEFT-TO-RIGHT
