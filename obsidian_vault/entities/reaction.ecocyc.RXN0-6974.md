---
entity_id: "reaction.ecocyc.RXN0-6974"
entity_type: "reaction"
name: "RXN0-6974"
source_database: "EcoCyc"
source_id: "RXN0-6974"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6974

`reaction.ecocyc.RXN0-6974`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6974`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN. EcoCyc reaction equation: CPD-13393 + WATER -> GLY + MET; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Biological Role

Substrates: H2O (molecule.C00001), glycyl-L-methionine (molecule.ecocyc.CPD-13393). Products: Glycine (molecule.C00037), L-Methionine (molecule.C00073).

## Annotation

This reaction is needed because automated instantiation of this case fails for the generic version 3.4.13.18-RXN.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13393|molecule.ecocyc.CPD-13393]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6974`

## Notes

CPD-13393 + WATER -> GLY + MET; direction=PHYSIOL-LEFT-TO-RIGHT
