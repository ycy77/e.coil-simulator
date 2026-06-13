---
entity_id: "reaction.ecocyc.TRANS-RXN-250"
entity_type: "reaction"
name: "TRANS-RXN-250"
source_database: "EcoCyc"
source_id: "TRANS-RXN-250"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Mg2+-importing ATPase"
  - "Magnesium-translocating P-type ATPase"
---

# TRANS-RXN-250

`reaction.ecocyc.TRANS-RXN-250`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-250`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MG+2 + WATER + ATP -> MG+2 + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MG+2 + WATER + ATP -> MG+2 + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Mg2+ transporting P-type ATPase (complex.ecocyc.CPLX0-13311). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Magnesium cation (molecule.C00305). Products: ADP (molecule.C00008), H+ (molecule.C00080), Magnesium cation (molecule.C00305), phosphate (molecule.ecocyc.Pi).

## Annotation

MG+2 + WATER + ATP -> MG+2 + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-13311|complex.ecocyc.CPLX0-13311]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-250`

## Notes

MG+2 + WATER + ATP -> MG+2 + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
