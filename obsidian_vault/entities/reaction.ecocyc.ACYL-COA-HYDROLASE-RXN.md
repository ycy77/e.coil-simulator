---
entity_id: "reaction.ecocyc.ACYL-COA-HYDROLASE-RXN"
entity_type: "reaction"
name: "ACYL-COA-HYDROLASE-RXN"
source_database: "EcoCyc"
source_id: "ACYL-COA-HYDROLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACYL-COA-HYDROLASE-RXN

`reaction.ecocyc.ACYL-COA-HYDROLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACYL-COA-HYDROLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACYL-COA + WATER -> CO-A + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACYL-COA + WATER -> CO-A + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acyl-CoA thioesterase II (complex.ecocyc.THIOESTERII-CPLX), yciA (protein.P0A8Z0), yigI (protein.P0ADP2). Substrates: H2O (molecule.C00001), Acyl-CoA (molecule.C00040). Products: CoA (molecule.C00010), H+ (molecule.C00080), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

ACYL-COA + WATER -> CO-A + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.THIOESTERII-CPLX|complex.ecocyc.THIOESTERII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A8Z0|protein.P0A8Z0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ADP2|protein.P0ADP2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00040|molecule.C00040]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1625|molecule.ecocyc.CPD0-1625]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACYL-COA-HYDROLASE-RXN`

## Notes

ACYL-COA + WATER -> CO-A + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
