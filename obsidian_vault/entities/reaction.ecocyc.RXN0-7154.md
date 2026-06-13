---
entity_id: "reaction.ecocyc.RXN0-7154"
entity_type: "reaction"
name: "RXN0-7154"
source_database: "EcoCyc"
source_id: "RXN0-7154"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7154

`reaction.ecocyc.RXN0-7154`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7154`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16716 + NADP -> CPD0-2582 + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-16716 + NADP -> CPD0-2582 + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by NADPH-dependent aldehyde reductase YqhD (complex.ecocyc.CPLX0-7667). Substrates: NADP+ (molecule.C00006), 1,3,4-butanetriol (molecule.ecocyc.CPD-16716). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (3R)-3,4-dihydroxybutanal (molecule.ecocyc.CPD0-2582).

## Annotation

CPD-16716 + NADP -> CPD0-2582 + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7667|complex.ecocyc.CPLX0-7667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2582|molecule.ecocyc.CPD0-2582]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16716|molecule.ecocyc.CPD-16716]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7154`

## Notes

CPD-16716 + NADP -> CPD0-2582 + NADPH + PROTON; direction=REVERSIBLE
