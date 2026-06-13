---
entity_id: "reaction.ecocyc.RXN0-6482"
entity_type: "reaction"
name: "RXN0-6482"
source_database: "EcoCyc"
source_id: "RXN0-6482"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6482

`reaction.ecocyc.RXN0-6482`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6482`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2353 + Pi -> tRNAs + tRNA-fragment; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2353 + Pi -> tRNAs + tRNA-fragment; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribonuclease T (complex.ecocyc.CPLX0-3602), rph (protein.P0CG19). Substrates: phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

CPD0-2353 + Pi -> tRNAs + tRNA-fragment; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3602|complex.ecocyc.CPLX0-3602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0CG19|protein.P0CG19]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6482`

## Notes

CPD0-2353 + Pi -> tRNAs + tRNA-fragment; direction=LEFT-TO-RIGHT
