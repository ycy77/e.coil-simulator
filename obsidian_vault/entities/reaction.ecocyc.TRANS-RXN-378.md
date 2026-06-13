---
entity_id: "reaction.ecocyc.TRANS-RXN-378"
entity_type: "reaction"
name: "TRANS-RXN-378"
source_database: "EcoCyc"
source_id: "TRANS-RXN-378"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-378

`reaction.ecocyc.TRANS-RXN-378`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-378`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

Polymyxins + ATP + WATER -> Polymyxins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Polymyxins + ATP + WATER -> Polymyxins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ABC-type tripartite efflux pump (complex.ecocyc.TRANS-200-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a polymyxin (molecule.ecocyc.Polymyxins). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), a polymyxin (molecule.ecocyc.Polymyxins).

## Annotation

Polymyxins + ATP + WATER -> Polymyxins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Polymyxins|molecule.ecocyc.Polymyxins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Polymyxins|molecule.ecocyc.Polymyxins]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-378`

## Notes

Polymyxins + ATP + WATER -> Polymyxins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
