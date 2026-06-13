---
entity_id: "reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN"
entity_type: "reaction"
name: "N-ACETYLGLUTPREDUCT-RXN"
source_database: "EcoCyc"
source_id: "N-ACETYLGLUTPREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# N-ACETYLGLUTPREDUCT-RXN

`reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:N-ACETYLGLUTPREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in arginine biosynthesis. EcoCyc reaction equation: CPD-469 + NADP + Pi -> PROTON + N-ACETYL-GLUTAMYL-P + NADPH; direction=REVERSIBLE. This is the third step in arginine biosynthesis.

## Biological Role

Catalyzed by argC (protein.P11446). Substrates: NADP+ (molecule.C00006), N-Acetyl-L-glutamate 5-semialdehyde (molecule.C01250), phosphate (molecule.ecocyc.Pi). Products: NADPH (molecule.C00005), H+ (molecule.C00080), N-Acetyl-L-glutamate 5-phosphate (molecule.C04133).

## Enriched Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Annotation

This is the third step in arginine biosynthesis.

## Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[protein.P11446|protein.P11446]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04133|molecule.C04133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01250|molecule.C01250]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfhydryl-Reagents|molecule.ecocyc.Sulfhydryl-Reagents]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:N-ACETYLGLUTPREDUCT-RXN`

## Notes

CPD-469 + NADP + Pi -> PROTON + N-ACETYL-GLUTAMYL-P + NADPH; direction=REVERSIBLE
