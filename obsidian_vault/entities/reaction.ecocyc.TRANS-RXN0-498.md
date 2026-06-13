---
entity_id: "reaction.ecocyc.TRANS-RXN0-498"
entity_type: "reaction"
name: "export of F-"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-498"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# export of F-

`reaction.ecocyc.TRANS-RXN0-498`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-498`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

F- -> F-; direction=REVERSIBLE EcoCyc reaction equation: F- -> F-; direction=REVERSIBLE.

## Biological Role

Catalyzed by F- channel (complex.ecocyc.CPLX0-8271). Substrates: fluoride (molecule.ecocyc.F-). Products: fluoride (molecule.ecocyc.F-).

## Annotation

F- -> F-; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8271|complex.ecocyc.CPLX0-8271]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-498`

## Notes

F- -> F-; direction=REVERSIBLE
