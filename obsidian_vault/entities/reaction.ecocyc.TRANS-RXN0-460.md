---
entity_id: "reaction.ecocyc.TRANS-RXN0-460"
entity_type: "reaction"
name: "TRANS-RXN0-460"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-460"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-460

`reaction.ecocyc.TRANS-RXN0-460`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-460`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli is urease negative - there is no significant degradation of urea and it is excreted into the culture medium EcoCyc reaction equation: UREA -> UREA; direction=REVERSIBLE. E. coli is urease negative - there is no significant degradation of urea and it is excreted into the culture medium

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: Urea (molecule.C00086). Products: Urea (molecule.C00086).

## Annotation

E. coli is urease negative - there is no significant degradation of urea and it is excreted into the culture medium

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00086|molecule.C00086]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00086|molecule.C00086]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-460`

## Notes

UREA -> UREA; direction=REVERSIBLE
