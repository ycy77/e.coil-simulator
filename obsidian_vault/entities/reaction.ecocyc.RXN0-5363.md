---
entity_id: "reaction.ecocyc.RXN0-5363"
entity_type: "reaction"
name: "RXN0-5363"
source_database: "EcoCyc"
source_id: "RXN0-5363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5363

`reaction.ecocyc.RXN0-5363`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5363`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15972 -> ALLOLACTOSE; direction=REVERSIBLE EcoCyc reaction equation: CPD-15972 -> ALLOLACTOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX). Substrates: Lactose (molecule.C00243). Products: allolactose (molecule.ecocyc.ALLOLACTOSE).

## Annotation

CPD-15972 -> ALLOLACTOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.ALLOLACTOSE|molecule.ecocyc.ALLOLACTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5363`

## Notes

CPD-15972 -> ALLOLACTOSE; direction=REVERSIBLE
