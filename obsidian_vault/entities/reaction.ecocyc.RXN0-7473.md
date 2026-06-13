---
entity_id: "reaction.ecocyc.RXN0-7473"
entity_type: "reaction"
name: "RXN0-7473"
source_database: "EcoCyc"
source_id: "RXN0-7473"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7473

`reaction.ecocyc.RXN0-7473`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7473`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2353 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2353 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ribonuclease BN (complex.ecocyc.CPLX0-3601), ribonuclease T (complex.ecocyc.CPLX0-3602), rnd (protein.P09155), rph (protein.P0CG19). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-8469` polycistronic tRNA processing I (EcoCyc)
- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)
- `ecocyc.PWY0-1626` polycistronic tRNA processing III (EcoCyc)
- `ecocyc.PWY0-1627` polycistronic tRNA processing IV (EcoCyc)

## Annotation

CPD0-2353 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8469` polycistronic tRNA processing I (EcoCyc)
- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)
- `ecocyc.PWY0-1626` polycistronic tRNA processing III (EcoCyc)
- `ecocyc.PWY0-1627` polycistronic tRNA processing IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3601|complex.ecocyc.CPLX0-3601]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3602|complex.ecocyc.CPLX0-3602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P09155|protein.P09155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0CG19|protein.P0CG19]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7473`

## Notes

CPD0-2353 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
