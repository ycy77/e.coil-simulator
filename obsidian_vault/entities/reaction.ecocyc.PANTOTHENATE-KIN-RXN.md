---
entity_id: "reaction.ecocyc.PANTOTHENATE-KIN-RXN"
entity_type: "reaction"
name: "PANTOTHENATE-KIN-RXN"
source_database: "EcoCyc"
source_id: "PANTOTHENATE-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PANTOTHENATE-KIN-RXN

`reaction.ecocyc.PANTOTHENATE-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PANTOTHENATE-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in coenzyme A (CoA) biosynthesis. EcoCyc reaction equation: PANTOTHENATE + ATP -> PROTON + 4-P-PANTOTHENATE + ADP; direction=LEFT-TO-RIGHT. This reaction is involved in coenzyme A (CoA) biosynthesis.

## Biological Role

Catalyzed by pantothenate kinase / pantetheine kinase (complex.ecocyc.PANTOTHENATE-KIN-CPLX). Substrates: ATP (molecule.C00002), Pantothenate (molecule.C00864). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-4'-Phosphopantothenate (molecule.C03492).

## Enriched Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Annotation

This reaction is involved in coenzyme A (CoA) biosynthesis.

## Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.PANTOTHENATE-KIN-CPLX|complex.ecocyc.PANTOTHENATE-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03492|molecule.C03492]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00864|molecule.C00864]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1152|molecule.ecocyc.CPD0-1152]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1153|molecule.ecocyc.CPD0-1153]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PANTOTHENATE-KIN-RXN`

## Notes

PANTOTHENATE + ATP -> PROTON + 4-P-PANTOTHENATE + ADP; direction=LEFT-TO-RIGHT
