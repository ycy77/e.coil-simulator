---
entity_id: "reaction.ecocyc.RXN-5921"
entity_type: "reaction"
name: "RXN-5921"
source_database: "EcoCyc"
source_id: "RXN-5921"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-5921

`reaction.ecocyc.RXN-5921`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-5921`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARNITINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> CPD-16618 + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CARNITINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> CPD-16618 + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by carnitine monooxygenase (complex.ecocyc.CPLX0-8232). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), L-carnitine (molecule.ecocyc.CARNITINE), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: H2O (molecule.C00001), Trimethylamine (molecule.C00565), L-malic semialdehyde (molecule.ecocyc.CPD-16618), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

CARNITINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> CPD-16618 + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8232|complex.ecocyc.CPLX0-8232]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16618|molecule.ecocyc.CPD-16618]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CARNITINE|molecule.ecocyc.CARNITINE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-5921`

## Notes

CARNITINE + OXYGEN-MOLECULE + NADH-P-OR-NOP + PROTON -> CPD-16618 + TRIMETHYLAMINE + NAD-P-OR-NOP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
