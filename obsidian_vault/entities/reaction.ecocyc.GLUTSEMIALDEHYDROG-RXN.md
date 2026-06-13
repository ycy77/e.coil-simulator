---
entity_id: "reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN"
entity_type: "reaction"
name: "GLUTSEMIALDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "GLUTSEMIALDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTSEMIALDEHYDROG-RXN

`reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTSEMIALDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-GLUTAMATE_GAMMA-SEMIALDEHYDE + Pi + NADP -> L-GLUTAMATE-5-P + NADPH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: L-GLUTAMATE_GAMMA-SEMIALDEHYDE + Pi + NADP -> L-GLUTAMATE-5-P + NADPH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by glutamate-5-semialdehyde dehydrogenase (complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX). Substrates: NADP+ (molecule.C00006), L-Glutamate 5-semialdehyde (molecule.C01165), phosphate (molecule.ecocyc.Pi). Products: NADPH (molecule.C00005), H+ (molecule.C00080), L-Glutamyl 5-phosphate (molecule.C03287).

## Enriched Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)

## Annotation

L-GLUTAMATE_GAMMA-SEMIALDEHYDE + Pi + NADP -> L-GLUTAMATE-5-P + NADPH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX|complex.ecocyc.GLUTSEMIALDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03287|molecule.C03287]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01165|molecule.C01165]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1454|molecule.ecocyc.CPD0-1454]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTSEMIALDEHYDROG-RXN`

## Notes

L-GLUTAMATE_GAMMA-SEMIALDEHYDE + Pi + NADP -> L-GLUTAMATE-5-P + NADPH + PROTON; direction=RIGHT-TO-LEFT
