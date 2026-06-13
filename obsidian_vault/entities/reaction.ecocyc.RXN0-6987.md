---
entity_id: "reaction.ecocyc.RXN0-6987"
entity_type: "reaction"
name: "RXN0-6987"
source_database: "EcoCyc"
source_id: "RXN0-6987"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6987

`reaction.ecocyc.RXN0-6987`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6987`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN. EcoCyc reaction equation: CPD-13406 + WATER -> GLY + L-ASPARTATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Biological Role

Substrates: H2O (molecule.C00001), glycyl-L-aspartate (molecule.ecocyc.CPD-13406). Products: Glycine (molecule.C00037), L-Aspartate (molecule.C00049).

## Annotation

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13406|molecule.ecocyc.CPD-13406]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6987`

## Notes

CPD-13406 + WATER -> GLY + L-ASPARTATE; direction=PHYSIOL-LEFT-TO-RIGHT
