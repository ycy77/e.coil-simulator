---
entity_id: "reaction.ecocyc.RXN0-1804"
entity_type: "reaction"
name: "RXN0-1804"
source_database: "EcoCyc"
source_id: "RXN0-1804"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1804

`reaction.ecocyc.RXN0-1804`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1804`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltose outer membrane channel / phage lambda receptor protein (complex.ecocyc.CPLX0-7655). Substrates: non-specific ion/solute (molecule.ecocyc.Unspecified-Ion-Or-Solute). Products: non-specific ion/solute (molecule.ecocyc.Unspecified-Ion-Or-Solute).

## Annotation

Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7655|complex.ecocyc.CPLX0-7655]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Unspecified-Ion-Or-Solute|molecule.ecocyc.Unspecified-Ion-Or-Solute]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Unspecified-Ion-Or-Solute|molecule.ecocyc.Unspecified-Ion-Or-Solute]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1804`

## Notes

Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=LEFT-TO-RIGHT
