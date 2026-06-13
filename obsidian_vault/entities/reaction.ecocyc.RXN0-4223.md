---
entity_id: "reaction.ecocyc.RXN0-4223"
entity_type: "reaction"
name: "3'-exoribonuclease"
source_database: "EcoCyc"
source_id: "RXN0-4223"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3'-exoribonuclease

`reaction.ecocyc.RXN0-4223`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4223`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reaction is the exoribonucleolytic cleavage of stable RNA to yield 5'-phosphomonoesters. EcoCyc reaction equation: RNA-Holder + WATER -> RNA-Holder + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. The reaction is the exoribonucleolytic cleavage of stable RNA to yield 5'-phosphomonoesters.

## Biological Role

Catalyzed by ribonuclease T (complex.ecocyc.CPLX0-3602), tatD (protein.P27859). Substrates: H2O (molecule.C00001), RNA (molecule.C00046). Products: RNA (molecule.C00046), a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates).

## Annotation

The reaction is the exoribonucleolytic cleavage of stable RNA to yield 5'-phosphomonoesters.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3602|complex.ecocyc.CPLX0-3602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27859|protein.P27859]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4223`

## Notes

RNA-Holder + WATER -> RNA-Holder + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
