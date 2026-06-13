---
entity_id: "reaction.ecocyc.HOMOSERKIN-RXN"
entity_type: "reaction"
name: "HOMOSERKIN-RXN"
source_database: "EcoCyc"
source_id: "HOMOSERKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOMOSERKIN-RXN

`reaction.ecocyc.HOMOSERKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOMOSERKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first of the two enzymes leading to the biosynthesis of L-threonine from L-homoserine. This is the first reaction after the branch-point to methionine. EcoCyc reaction equation: HOMO-SER + ATP -> PROTON + O-PHOSPHO-L-HOMOSERINE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first of the two enzymes leading to the biosynthesis of L-threonine from L-homoserine. This is the first reaction after the branch-point to methionine.

## Biological Role

Catalyzed by homoserine kinase (complex.ecocyc.HOMOSERKIN-CPLX). Substrates: ATP (molecule.C00002), L-Homoserine (molecule.C00263). Products: ADP (molecule.C00008), H+ (molecule.C00080), O-Phospho-L-homoserine (molecule.C01102).

## Enriched Pathways

- `ecocyc.HOMOSER-THRESYN-PWY` L-threonine biosynthesis (EcoCyc)

## Annotation

This is the first of the two enzymes leading to the biosynthesis of L-threonine from L-homoserine. This is the first reaction after the branch-point to methionine.

## Pathways

- `ecocyc.HOMOSER-THRESYN-PWY` L-threonine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.HOMOSERKIN-CPLX|complex.ecocyc.HOMOSERKIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01102|molecule.C01102]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-Aminobutyrate|molecule.ecocyc.2-Aminobutyrate]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1475|molecule.ecocyc.CPD0-1475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HOMOSERKIN-RXN`

## Notes

HOMO-SER + ATP -> PROTON + O-PHOSPHO-L-HOMOSERINE + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
