---
entity_id: "reaction.ecocyc.RXN0-7241"
entity_type: "reaction"
name: "RXN0-7241"
source_database: "EcoCyc"
source_id: "RXN0-7241"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7241

`reaction.ecocyc.RXN0-7241`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7241`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Medium-chain-fatty-acids -> Medium-chain-fatty-acids; direction=REVERSIBLE EcoCyc reaction equation: Medium-chain-fatty-acids -> Medium-chain-fatty-acids; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: a medium chain fatty acid (molecule.ecocyc.Medium-chain-fatty-acids). Products: a medium chain fatty acid (molecule.ecocyc.Medium-chain-fatty-acids).

## Annotation

Medium-chain-fatty-acids -> Medium-chain-fatty-acids; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Medium-chain-fatty-acids|molecule.ecocyc.Medium-chain-fatty-acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Medium-chain-fatty-acids|molecule.ecocyc.Medium-chain-fatty-acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7241`

## Notes

Medium-chain-fatty-acids -> Medium-chain-fatty-acids; direction=REVERSIBLE
