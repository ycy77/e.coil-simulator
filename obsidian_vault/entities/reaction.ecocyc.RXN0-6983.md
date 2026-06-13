---
entity_id: "reaction.ecocyc.RXN0-6983"
entity_type: "reaction"
name: "RXN0-6983"
source_database: "EcoCyc"
source_id: "RXN0-6983"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6983

`reaction.ecocyc.RXN0-6983`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6983`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN. EcoCyc reaction equation: CPD-13394 + WATER -> GLY + GLN; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Biological Role

Substrates: H2O (molecule.C00001), glycyl-L-glutamine (molecule.ecocyc.CPD-13394). Products: Glycine (molecule.C00037), L-Glutamine (molecule.C00064).

## Annotation

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13394|molecule.ecocyc.CPD-13394]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6983`

## Notes

CPD-13394 + WATER -> GLY + GLN; direction=PHYSIOL-LEFT-TO-RIGHT
