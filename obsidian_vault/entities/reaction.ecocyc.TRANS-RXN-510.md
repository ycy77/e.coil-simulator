---
entity_id: "reaction.ecocyc.TRANS-RXN-510"
entity_type: "reaction"
name: "TRANS-RXN-510"
source_database: "EcoCyc"
source_id: "TRANS-RXN-510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-510

`reaction.ecocyc.TRANS-RXN-510`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-510`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

a-type-II-secretion-system-substrate + ATP + WATER -> a-type-II-secretion-system-substrate + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-type-II-secretion-system-substrate + ATP + WATER -> a-type-II-secretion-system-substrate + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by type II secretion system (complex.ecocyc.CPLX0-3382). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

a-type-II-secretion-system-substrate + ATP + WATER -> a-type-II-secretion-system-substrate + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-510`

## Notes

a-type-II-secretion-system-substrate + ATP + WATER -> a-type-II-secretion-system-substrate + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
