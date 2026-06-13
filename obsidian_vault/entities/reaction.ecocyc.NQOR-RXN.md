---
entity_id: "reaction.ecocyc.NQOR-RXN"
entity_type: "reaction"
name: "NQOR-RXN"
source_database: "EcoCyc"
source_id: "NQOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NQOR-RXN

`reaction.ecocyc.NQOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NQOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

The reaction is a two-electron reduction of quinones to quinols. EcoCyc reaction equation: ETR-Quinones + NADH-P-OR-NOP + PROTON -> ETR-Quinols + NAD-P-OR-NOP; direction=PHYSIOL-LEFT-TO-RIGHT. The reaction is a two-electron reduction of quinones to quinols.

## Biological Role

Catalyzed by quinone reductase (complex.ecocyc.CPLX0-3121), NAD(P)H:quinone oxidoreductase (complex.ecocyc.CPLX0-7632), regulator of KefC-mediated potassium transport and quinone oxidoreductase (complex.ecocyc.CPLX0-7939). Substrates: H+ (molecule.C00080), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

The reaction is a two-electron reduction of quinones to quinols.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3121|complex.ecocyc.CPLX0-3121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7632|complex.ecocyc.CPLX0-7632]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7939|complex.ecocyc.CPLX0-7939]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NQOR-RXN`

## Notes

ETR-Quinones + NADH-P-OR-NOP + PROTON -> ETR-Quinols + NAD-P-OR-NOP; direction=PHYSIOL-LEFT-TO-RIGHT
