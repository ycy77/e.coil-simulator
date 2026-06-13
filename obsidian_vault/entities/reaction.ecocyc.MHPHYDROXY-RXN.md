---
entity_id: "reaction.ecocyc.MHPHYDROXY-RXN"
entity_type: "reaction"
name: "MHPHYDROXY-RXN"
source_database: "EcoCyc"
source_id: "MHPHYDROXY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MHPHYDROXY-RXN

`reaction.ecocyc.MHPHYDROXY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MHPHYDROXY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the degradation of 3-(3-hydroxyphenyl)propionate. EcoCyc reaction equation: PROTON + 3-HYDROXYPHENYL-PROPIONATE + NADH + OXYGEN-MOLECULE -> WATER + 2-3-DIHYDROXYPHENYL-PROPIONATE + NAD; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in the degradation of 3-(3-hydroxyphenyl)propionate.

## Biological Role

Catalyzed by mhpA (protein.P77397). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), H+ (molecule.C00080), 3-(3-Hydroxyphenyl)propanoic acid (molecule.C11457). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), 3-(2,3-Dihydroxyphenyl)propanoate (molecule.C04044).

## Enriched Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

This is the first reaction in the degradation of 3-(3-hydroxyphenyl)propionate.

## Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P77397|protein.P77397]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04044|molecule.C04044]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11457|molecule.C11457]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MHPHYDROXY-RXN`

## Notes

PROTON + 3-HYDROXYPHENYL-PROPIONATE + NADH + OXYGEN-MOLECULE -> WATER + 2-3-DIHYDROXYPHENYL-PROPIONATE + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
