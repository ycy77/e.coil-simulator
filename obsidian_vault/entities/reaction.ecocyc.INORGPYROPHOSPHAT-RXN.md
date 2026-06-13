---
entity_id: "reaction.ecocyc.INORGPYROPHOSPHAT-RXN"
entity_type: "reaction"
name: "INORGPYROPHOSPHAT-RXN"
source_database: "EcoCyc"
source_id: "INORGPYROPHOSPHAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# INORGPYROPHOSPHAT-RXN

`reaction.ecocyc.INORGPYROPHOSPHAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:INORGPYROPHOSPHAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This reaction is part of central intermediary metabolism. It provides a thermodynamic pull for biosynthetic reactions that produce pyrophosphate. EcoCyc reaction equation: WATER + PPI -> PROTON + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of central intermediary metabolism. It provides a thermodynamic pull for biosynthetic reactions that produce pyrophosphate.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), inorganic pyrophosphatase (complex.ecocyc.CPLX0-243). Substrates: H2O (molecule.C00001), Diphosphate (molecule.C00013). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Annotation

This reaction is part of central intermediary metabolism. It provides a thermodynamic pull for biosynthetic reactions that produce pyrophosphate.

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-243|complex.ecocyc.CPLX0-243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:INORGPYROPHOSPHAT-RXN`

## Notes

WATER + PPI -> PROTON + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
