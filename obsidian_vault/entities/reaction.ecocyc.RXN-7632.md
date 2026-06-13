---
entity_id: "reaction.ecocyc.RXN-7632"
entity_type: "reaction"
name: "RXN-7632"
source_database: "EcoCyc"
source_id: "RXN-7632"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7632

`reaction.ecocyc.RXN-7632`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7632`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-6982 + NAD-P-OR-NOP -> 34-DIHYDROXYPHENYLPYRUVATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-6982 + NAD-P-OR-NOP -> 34-DIHYDROXYPHENYLPYRUVATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by hcxB (protein.P30178). Substrates: (R)-3-(3,4-Dihydroxyphenyl)lactate (molecule.C22038), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 3-(3,4-Dihydroxyphenyl)pyruvate (molecule.C04045), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

CPD-6982 + NAD-P-OR-NOP -> 34-DIHYDROXYPHENYLPYRUVATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P30178|protein.P30178]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04045|molecule.C04045]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C22038|molecule.C22038]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7632`

## Notes

CPD-6982 + NAD-P-OR-NOP -> 34-DIHYDROXYPHENYLPYRUVATE + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
