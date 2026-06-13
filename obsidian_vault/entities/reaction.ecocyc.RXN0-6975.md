---
entity_id: "reaction.ecocyc.RXN0-6975"
entity_type: "reaction"
name: "RXN0-6975"
source_database: "EcoCyc"
source_id: "RXN0-6975"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6975

`reaction.ecocyc.RXN0-6975`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6975`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN. EcoCyc reaction equation: CPD-13404 + WATER -> L-ALPHA-ALANINE + L-ASPARTATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Biological Role

Substrates: H2O (molecule.C00001), L-alanyl-L-aspartate (molecule.ecocyc.CPD-13404). Products: L-Alanine (molecule.C00041), L-Aspartate (molecule.C00049).

## Annotation

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13404|molecule.ecocyc.CPD-13404]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6975`

## Notes

CPD-13404 + WATER -> L-ALPHA-ALANINE + L-ASPARTATE; direction=PHYSIOL-LEFT-TO-RIGHT
