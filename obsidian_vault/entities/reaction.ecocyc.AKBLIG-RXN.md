---
entity_id: "reaction.ecocyc.AKBLIG-RXN"
entity_type: "reaction"
name: "AKBLIG-RXN"
source_database: "EcoCyc"
source_id: "AKBLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AKBLIG-RXN

`reaction.ecocyc.AKBLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AKBLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the primary route of threonine utilization, and is also a highly efficient alternate pathway for glycine and serine biosynthesis. EcoCyc reaction equation: GLY + ACETYL-COA -> AMINO-OXOBUT + CO-A; direction=REVERSIBLE. This reaction is part of the primary route of threonine utilization, and is also a highly efficient alternate pathway for glycine and serine biosynthesis.

## Biological Role

Catalyzed by 2-amino-3-ketobutyrate CoA ligase (complex.ecocyc.AKBLIG-CPLX). Substrates: Acetyl-CoA (molecule.C00024), Glycine (molecule.C00037). Products: CoA (molecule.C00010), L-2-Amino-3-oxobutanoic acid (molecule.C03508).

## Enriched Pathways

- `ecocyc.THREONINE-DEG2-PWY` L-threonine degradation II (EcoCyc)

## Annotation

This reaction is part of the primary route of threonine utilization, and is also a highly efficient alternate pathway for glycine and serine biosynthesis.

## Pathways

- `ecocyc.THREONINE-DEG2-PWY` L-threonine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `catalyzes` <-- [[complex.ecocyc.AKBLIG-CPLX|complex.ecocyc.AKBLIG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03508|molecule.C03508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00741|molecule.C00741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06105|molecule.C06105]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.AMINOMALONATE|molecule.ecocyc.AMINOMALONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13890|molecule.ecocyc.CPD-13890]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1074|molecule.ecocyc.CPD0-1074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLGLYOXAL|molecule.ecocyc.PHENYLGLYOXAL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AKBLIG-RXN`

## Notes

GLY + ACETYL-COA -> AMINO-OXOBUT + CO-A; direction=REVERSIBLE
