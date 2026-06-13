---
entity_id: "reaction.ecocyc.H2NEOPTERINALDOL-RXN"
entity_type: "reaction"
name: "H2NEOPTERINALDOL-RXN"
source_database: "EcoCyc"
source_id: "H2NEOPTERINALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# H2NEOPTERINALDOL-RXN

`reaction.ecocyc.H2NEOPTERINALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:H2NEOPTERINALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in the biosynthesis of folic acid. EcoCyc reaction equation: DIHYDRO-NEO-PTERIN -> GLYCOLALDEHYDE + AMINO-OH-HYDROXYMETHYL-DIHYDROPTERIDINE; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction in the biosynthesis of folic acid.

## Biological Role

Catalyzed by dihydroneopterin aldolase (complex.ecocyc.CPLX0-3936). Substrates: 7,8-Dihydroneopterin (molecule.C04874). Products: Glycolaldehyde (molecule.C00266), 6-(Hydroxymethyl)-7,8-dihydropterin (molecule.C01300).

## Enriched Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Annotation

This is a reaction in the biosynthesis of folic acid.

## Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3936|complex.ecocyc.CPLX0-3936]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01300|molecule.C01300]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04874|molecule.C04874]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:H2NEOPTERINALDOL-RXN`

## Notes

DIHYDRO-NEO-PTERIN -> GLYCOLALDEHYDE + AMINO-OH-HYDROXYMETHYL-DIHYDROPTERIDINE; direction=PHYSIOL-LEFT-TO-RIGHT
