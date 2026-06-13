---
entity_id: "reaction.ecocyc.TRANS-RXN0-563"
entity_type: "reaction"
name: "indole diffusion"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-563"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# indole diffusion

`reaction.ecocyc.TRANS-RXN0-563`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-563`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Indole rapidly crosses the inner membrane of E. coli K-12 without the need for a transport protein or channel. Indole diffuses across artifical lipid membranes EcoCyc reaction equation: INDOLE -> INDOLE; direction=REVERSIBLE. Indole rapidly crosses the inner membrane of E. coli K-12 without the need for a transport protein or channel. Indole diffuses across artifical lipid membranes

## Biological Role

Substrates: Indole (molecule.C00463). Products: Indole (molecule.C00463).

## Annotation

Indole rapidly crosses the inner membrane of E. coli K-12 without the need for a transport protein or channel. Indole diffuses across artifical lipid membranes

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-563`

## Notes

INDOLE -> INDOLE; direction=REVERSIBLE
