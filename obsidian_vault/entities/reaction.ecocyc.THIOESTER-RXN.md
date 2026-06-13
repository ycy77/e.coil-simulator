---
entity_id: "reaction.ecocyc.THIOESTER-RXN"
entity_type: "reaction"
name: "THIOESTER-RXN"
source_database: "EcoCyc"
source_id: "THIOESTER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THIOESTER-RXN

`reaction.ecocyc.THIOESTER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIOESTER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is part of the hydrolytic cleavage of fatty acyl thioesters. EcoCyc reaction equation: Saturated-Fatty-Acyl-CoA + WATER -> CPD66-39 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the hydrolytic cleavage of fatty acyl thioesters.

## Biological Role

Catalyzed by multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1 (complex.ecocyc.CPLX0-7630). Substrates: H2O (molecule.C00001), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA). Products: CoA (molecule.C00010), H+ (molecule.C00080), a 2,3,4-saturated fatty acid (molecule.ecocyc.CPD66-39).

## Annotation

This reaction is part of the hydrolytic cleavage of fatty acyl thioesters.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7630|complex.ecocyc.CPLX0-7630]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD66-39|molecule.ecocyc.CPD66-39]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE|molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THIOESTER-RXN`

## Notes

Saturated-Fatty-Acyl-CoA + WATER -> CPD66-39 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
