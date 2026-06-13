---
entity_id: "reaction.ecocyc.N-ACETYLTRANSFER-RXN"
entity_type: "reaction"
name: "N-ACETYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "N-ACETYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# N-ACETYLTRANSFER-RXN

`reaction.ecocyc.N-ACETYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:N-ACETYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in arginine biosynthesis. EcoCyc reaction equation: GLT + ACETYL-COA -> PROTON + ACETYL-GLU + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first step in arginine biosynthesis.

## Biological Role

Catalyzed by N-acetylglutamate synthase (complex.ecocyc.N-ACETYLTRANSFER-CPLX). Substrates: Acetyl-CoA (molecule.C00024), L-Glutamate (molecule.C00025). Products: CoA (molecule.C00010), H+ (molecule.C00080), N-Acetyl-L-glutamate (molecule.C00624).

## Enriched Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Annotation

This is the first step in arginine biosynthesis.

## Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.N-ACETYLTRANSFER-CPLX|complex.ecocyc.N-ACETYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00624|molecule.C00624]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00327|molecule.C00327]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1690|molecule.ecocyc.CPD0-1690]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1691|molecule.ecocyc.CPD0-1691]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:N-ACETYLTRANSFER-RXN`

## Notes

GLT + ACETYL-COA -> PROTON + ACETYL-GLU + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
