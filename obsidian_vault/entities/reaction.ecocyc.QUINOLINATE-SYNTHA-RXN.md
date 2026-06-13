---
entity_id: "reaction.ecocyc.QUINOLINATE-SYNTHA-RXN"
entity_type: "reaction"
name: "QUINOLINATE-SYNTHA-RXN"
source_database: "EcoCyc"
source_id: "QUINOLINATE-SYNTHA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# QUINOLINATE-SYNTHA-RXN

`reaction.ecocyc.QUINOLINATE-SYNTHA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:QUINOLINATE-SYNTHA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in quinolinate biosynthesis, required for the de novo biosynthesis of NAD. EcoCyc reaction equation: IMINOASPARTATE + DIHYDROXY-ACETONE-PHOSPHATE -> QUINOLINATE + WATER + Pi; direction=LEFT-TO-RIGHT. A reaction in quinolinate biosynthesis, required for the de novo biosynthesis of NAD.

## Biological Role

Catalyzed by quinolinate synthase (complex.ecocyc.CPLX0-7719). Substrates: Glycerone phosphate (molecule.C00111), Iminoaspartate (molecule.C05840). Products: H2O (molecule.C00001), Quinolinate (molecule.C03722), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Annotation

A reaction in quinolinate biosynthesis, required for the de novo biosynthesis of NAD.

## Pathways

- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7719|complex.ecocyc.CPLX0-7719]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03722|molecule.C03722]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05840|molecule.C05840]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:QUINOLINATE-SYNTHA-RXN`

## Notes

IMINOASPARTATE + DIHYDROXY-ACETONE-PHOSPHATE -> QUINOLINATE + WATER + Pi; direction=LEFT-TO-RIGHT
