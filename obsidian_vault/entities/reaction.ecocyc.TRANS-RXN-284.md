---
entity_id: "reaction.ecocyc.TRANS-RXN-284"
entity_type: "reaction"
name: "hydrogen peroxide diffusion"
source_database: "EcoCyc"
source_id: "TRANS-RXN-284"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG|CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hydrogen peroxide diffusion

`reaction.ecocyc.TRANS-RXN-284`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-284`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG|CCO-OUTER-MEM

## Enriched Summary

H2O2 crosses membranes with an efficiency similar to water . The outer membrane of E. coli K-12 is approximately 30 times more permeable to hydrogen peroxide than the inner membrane . EcoCyc reaction equation: HYDROGEN-PEROXIDE -> HYDROGEN-PEROXIDE; direction=REVERSIBLE. H2O2 crosses membranes with an efficiency similar to water . The outer membrane of E. coli K-12 is approximately 30 times more permeable to hydrogen peroxide than the inner membrane .

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027). Products: Hydrogen peroxide (molecule.C00027).

## Annotation

H2O2 crosses membranes with an efficiency similar to water . The outer membrane of E. coli K-12 is approximately 30 times more permeable to hydrogen peroxide than the inner membrane .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-284`

## Notes

HYDROGEN-PEROXIDE -> HYDROGEN-PEROXIDE; direction=REVERSIBLE
