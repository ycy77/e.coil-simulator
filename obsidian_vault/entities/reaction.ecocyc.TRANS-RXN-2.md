---
entity_id: "reaction.ecocyc.TRANS-RXN-2"
entity_type: "reaction"
name: "TRANS-RXN-2"
source_database: "EcoCyc"
source_id: "TRANS-RXN-2"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "K(+)-transporting ATPase"
  - "Potassium-importing ATPase"
  - "K(+)-importing ATPase"
---

# TRANS-RXN-2

`reaction.ecocyc.TRANS-RXN-2`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-2`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

K+ + WATER + ATP -> K+ + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: K+ + WATER + ATP -> K+ + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by K+ transporting P-type ATPase (complex.ecocyc.ATPASE-1-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Potassium cation (molecule.C00238). Products: ADP (molecule.C00008), H+ (molecule.C00080), Potassium cation (molecule.C00238), phosphate (molecule.ecocyc.Pi).

## Annotation

K+ + WATER + ATP -> K+ + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.ATPASE-1-CPLX|complex.ecocyc.ATPASE-1-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-10322|molecule.ecocyc.CPD-10322]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4584|molecule.ecocyc.CPD-4584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-2`

## Notes

K+ + WATER + ATP -> K+ + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
