---
entity_id: "reaction.ecocyc.RXN-15892"
entity_type: "reaction"
name: "RXN-15892"
source_database: "EcoCyc"
source_id: "RXN-15892"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15892

`reaction.ecocyc.RXN-15892`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15892`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8938 + WATER + NAD-P-OR-NOP -> CPD-17129 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8938 + WATER + NAD-P-OR-NOP -> CPD-17129 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), 3,6-anhydro-L-galactofuranose (molecule.ecocyc.CPD-8938), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 3,6-Anhydro-L-galactonate (molecule.C20903), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

CPD-8938 + WATER + NAD-P-OR-NOP -> CPD-17129 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20903|molecule.C20903]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8938|molecule.ecocyc.CPD-8938]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15892`

## Notes

CPD-8938 + WATER + NAD-P-OR-NOP -> CPD-17129 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
