---
entity_id: "reaction.ecocyc.RXN0-7246"
entity_type: "reaction"
name: "RXN0-7246"
source_database: "EcoCyc"
source_id: "RXN0-7246"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7246

`reaction.ecocyc.RXN0-7246`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7246`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Lactones -> Lactones; direction=REVERSIBLE EcoCyc reaction equation: Lactones -> Lactones; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: a lactone (molecule.ecocyc.Lactones). Products: a lactone (molecule.ecocyc.Lactones).

## Annotation

Lactones -> Lactones; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Lactones|molecule.ecocyc.Lactones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Lactones|molecule.ecocyc.Lactones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7246`

## Notes

Lactones -> Lactones; direction=REVERSIBLE
