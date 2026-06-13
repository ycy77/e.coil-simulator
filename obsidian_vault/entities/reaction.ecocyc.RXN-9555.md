---
entity_id: "reaction.ecocyc.RXN-9555"
entity_type: "reaction"
name: "RXN-9555"
source_database: "EcoCyc"
source_id: "RXN-9555"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9555

`reaction.ecocyc.RXN-9555`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9555`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Cis-vaccenoyl-ACPs + WATER -> CPD-9247 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Cis-vaccenoyl-ACPs + WATER -> CPD-9247 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1 (complex.ecocyc.CPLX0-7630). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), cis-vaccenate (molecule.ecocyc.CPD-9247).

## Enriched Pathways

- `ecocyc.PWY-5973` cis-vaccenate biosynthesis (EcoCyc)

## Annotation

Cis-vaccenoyl-ACPs + WATER -> CPD-9247 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5973` cis-vaccenate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7630|complex.ecocyc.CPLX0-7630]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9247|molecule.ecocyc.CPD-9247]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9555`

## Notes

Cis-vaccenoyl-ACPs + WATER -> CPD-9247 + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
