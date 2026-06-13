---
entity_id: "reaction.ecocyc.CHEBDEP-RXN"
entity_type: "reaction"
name: "CHEBDEP-RXN"
source_database: "EcoCyc"
source_id: "CHEBDEP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHEBDEP-RXN

`reaction.ecocyc.CHEBDEP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHEBDEP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-CHEB + WATER -> Pi + CHEB-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-CHEB + WATER -> Pi + CHEB-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

PHOSPHO-CHEB + WATER -> Pi + CHEB-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CHEBDEP-RXN`

## Notes

PHOSPHO-CHEB + WATER -> Pi + CHEB-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT
