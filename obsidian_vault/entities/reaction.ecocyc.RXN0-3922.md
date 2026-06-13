---
entity_id: "reaction.ecocyc.RXN0-3922"
entity_type: "reaction"
name: "RXN0-3922"
source_database: "EcoCyc"
source_id: "RXN0-3922"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3922

`reaction.ecocyc.RXN0-3922`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3922`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + NAD-P-OR-NOP + WATER -> CPD-9000 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + NAD-P-OR-NOP + WATER -> CPD-9000 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by puuC (protein.P23883). Substrates: H2O (molecule.C00001), gamma-Glutamyl-gamma-aminobutyraldehyde (molecule.C15700), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 4-(L-gamma-Glutamylamino)butanoate (molecule.C15767), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Annotation

GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + NAD-P-OR-NOP + WATER -> CPD-9000 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P23883|protein.P23883]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15767|molecule.C15767]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15700|molecule.C15700]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3922`

## Notes

GAMMA-GLUTAMYL-GAMMA-AMINOBUTYRALDEH + NAD-P-OR-NOP + WATER -> CPD-9000 + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
