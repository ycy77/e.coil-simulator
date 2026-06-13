---
entity_id: "reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN"
entity_type: "reaction"
name: "FOLYLPOLYGLUTAMATESYNTH-RXN"
source_database: "EcoCyc"
source_id: "FOLYLPOLYGLUTAMATESYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Folylpoly-&gamma"
  - "-glutamate synthetase"
  - "Folate polyglutamate synthetase"
  - "Folylpolyglutamyl synthetase"
---

# FOLYLPOLYGLUTAMATESYNTH-RXN

`reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FOLYLPOLYGLUTAMATESYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the conversion of folates to polyglutamate derivatives. EcoCyc reaction equation: THF-GLU-N + GLT + ATP -> THF-GLU-N + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in the conversion of folates to polyglutamate derivatives.

## Biological Role

Catalyzed by folC (protein.P08192), folylpoly-α-glutamate synthetase (protein.ecocyc.MONOMER0-1661). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), THF-polyglutamate (molecule.C03541). Products: ADP (molecule.C00008), THF-polyglutamate (molecule.C03541), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)

## Annotation

This reaction is involved in the conversion of folates to polyglutamate derivatives.

## Pathways

- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[protein.P08192|protein.P08192]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.ecocyc.MONOMER0-1661|protein.ecocyc.MONOMER0-1661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00415|molecule.C00415]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00440|molecule.C00440]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00921|molecule.C00921]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1255|molecule.ecocyc.CPD0-1255]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1596|molecule.ecocyc.CPD0-1596]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FOLYLPOLYGLUTAMATESYNTH-RXN`

## Notes

THF-GLU-N + GLT + ATP -> THF-GLU-N + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
