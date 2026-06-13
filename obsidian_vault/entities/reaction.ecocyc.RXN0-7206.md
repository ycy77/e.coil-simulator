---
entity_id: "reaction.ecocyc.RXN0-7206"
entity_type: "reaction"
name: "RXN0-7206"
source_database: "EcoCyc"
source_id: "RXN0-7206"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7206

`reaction.ecocyc.RXN0-7206`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7206`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Aromatics -> Aromatics; direction=REVERSIBLE EcoCyc reaction equation: Aromatics -> Aromatics; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: an aromatic compound (molecule.ecocyc.Aromatics). Products: an aromatic compound (molecule.ecocyc.Aromatics).

## Annotation

Aromatics -> Aromatics; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Aromatics|molecule.ecocyc.Aromatics]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Aromatics|molecule.ecocyc.Aromatics]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7206`

## Notes

Aromatics -> Aromatics; direction=REVERSIBLE
