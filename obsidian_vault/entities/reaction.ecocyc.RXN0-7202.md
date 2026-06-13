---
entity_id: "reaction.ecocyc.RXN0-7202"
entity_type: "reaction"
name: "RXN0-7202"
source_database: "EcoCyc"
source_id: "RXN0-7202"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7202

`reaction.ecocyc.RXN0-7202`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7202`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

OLIGOPEPTIDES -> OLIGOPEPTIDES; direction=REVERSIBLE EcoCyc reaction equation: OLIGOPEPTIDES -> OLIGOPEPTIDES; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: Oligopeptide (molecule.C00098). Products: Oligopeptide (molecule.C00098).

## Annotation

OLIGOPEPTIDES -> OLIGOPEPTIDES; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00098|molecule.C00098]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00098|molecule.C00098]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7202`

## Notes

OLIGOPEPTIDES -> OLIGOPEPTIDES; direction=REVERSIBLE
