---
entity_id: "reaction.ecocyc.RXN0-5114"
entity_type: "reaction"
name: "RXN0-5114"
source_database: "EcoCyc"
source_id: "RXN0-5114"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5114

`reaction.ecocyc.RXN0-5114`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5114`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

3-P-SERINE + WATER -> SER + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-P-SERINE + WATER -> SER + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX), serB (protein.P0AGB0). Substrates: H2O (molecule.C00001), O-Phospho-L-serine (molecule.C01005). Products: L-Serine (molecule.C00065), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Annotation

3-P-SERINE + WATER -> SER + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AGB0|protein.P0AGB0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01005|molecule.C01005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5114`

## Notes

3-P-SERINE + WATER -> SER + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
