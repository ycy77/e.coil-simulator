---
entity_id: "reaction.ecocyc.RXN0-5455"
entity_type: "reaction"
name: "RXN0-5455"
source_database: "EcoCyc"
source_id: "RXN0-5455"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5455

`reaction.ecocyc.RXN0-5455`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5455`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROXYPROPANAL + NAD-P-OR-NOP + WATER -> 3-HYDROXY-PROPIONATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HYDROXYPROPANAL + NAD-P-OR-NOP + WATER -> 3-HYDROXY-PROPIONATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by puuC (protein.P23883). Substrates: H2O (molecule.C00001), 3-Hydroxypropanal (molecule.C00969), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 3-Hydroxypropanoate (molecule.C01013), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

HYDROXYPROPANAL + NAD-P-OR-NOP + WATER -> 3-HYDROXY-PROPIONATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23883|protein.P23883]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01013|molecule.C01013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00969|molecule.C00969]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5455`

## Notes

HYDROXYPROPANAL + NAD-P-OR-NOP + WATER -> 3-HYDROXY-PROPIONATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
