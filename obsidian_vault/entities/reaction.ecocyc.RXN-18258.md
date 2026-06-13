---
entity_id: "reaction.ecocyc.RXN-18258"
entity_type: "reaction"
name: "RXN-18258"
source_database: "EcoCyc"
source_id: "RXN-18258"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18258

`reaction.ecocyc.RXN-18258`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18258`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GAMMA-BUTYROBETAINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> SUCC-S-ALD + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GAMMA-BUTYROBETAINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> SUCC-S-ALD + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by carnitine monooxygenase (complex.ecocyc.CPLX0-8232). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), 4-Trimethylammoniobutanoate (molecule.C01181), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: H2O (molecule.C00001), Succinate semialdehyde (molecule.C00232), Trimethylamine (molecule.C00565), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

GAMMA-BUTYROBETAINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> SUCC-S-ALD + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8232|complex.ecocyc.CPLX0-8232]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00232|molecule.C00232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01181|molecule.C01181]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18258`

## Notes

GAMMA-BUTYROBETAINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> SUCC-S-ALD + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
