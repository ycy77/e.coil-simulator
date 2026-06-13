---
entity_id: "reaction.ecocyc.RXN0-4222"
entity_type: "reaction"
name: "RXN0-4222"
source_database: "EcoCyc"
source_id: "RXN0-4222"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4222

`reaction.ecocyc.RXN0-4222`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4222`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the exoribonucleolytic cleavage of tRNA precursor at the 3' terminus, yielding a 3'-hydroxyl and a 5'-phosphomonoester. EcoCyc reaction equation: CPD0-2351 + WATER -> CPD0-2354 + Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the exoribonucleolytic cleavage of tRNA precursor at the 3' terminus, yielding a 3'-hydroxyl and a 5'-phosphomonoester.

## Biological Role

Catalyzed by ribonuclease BN (complex.ecocyc.CPLX0-3601). Substrates: H2O (molecule.C00001). Products: a ribonucleoside 5'-monophosphate (molecule.ecocyc.Ribonucleoside-Monophosphates).

## Annotation

This reaction is the exoribonucleolytic cleavage of tRNA precursor at the 3' terminus, yielding a 3'-hydroxyl and a 5'-phosphomonoester.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3601|complex.ecocyc.CPLX0-3601]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleoside-Monophosphates|molecule.ecocyc.Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4222`

## Notes

CPD0-2351 + WATER -> CPD0-2354 + Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
