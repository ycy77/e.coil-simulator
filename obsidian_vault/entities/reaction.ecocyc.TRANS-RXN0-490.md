---
entity_id: "reaction.ecocyc.TRANS-RXN0-490"
entity_type: "reaction"
name: "TRANS-RXN0-490"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-490"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-490

`reaction.ecocyc.TRANS-RXN0-490`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-490`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

BETAINE -> BETAINE; direction=REVERSIBLE EcoCyc reaction equation: BETAINE -> BETAINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: Betaine (molecule.C00719). Products: Betaine (molecule.C00719).

## Annotation

BETAINE -> BETAINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-490`

## Notes

BETAINE -> BETAINE; direction=REVERSIBLE
