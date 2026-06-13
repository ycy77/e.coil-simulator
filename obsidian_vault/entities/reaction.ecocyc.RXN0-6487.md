---
entity_id: "reaction.ecocyc.RXN0-6487"
entity_type: "reaction"
name: "RXN0-6487"
source_database: "EcoCyc"
source_id: "RXN0-6487"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6487

`reaction.ecocyc.RXN0-6487`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6487`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-347 + NADP -> HYDROXYPROPANAL + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-347 + NADP -> HYDROXYPROPANAL + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by NADPH-dependent aldehyde reductase YqhD (complex.ecocyc.CPLX0-7667). Substrates: NADP+ (molecule.C00006), Propane-1,3-diol (molecule.C02457). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Hydroxypropanal (molecule.C00969).

## Annotation

CPD-347 + NADP -> HYDROXYPROPANAL + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7667|complex.ecocyc.CPLX0-7667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00969|molecule.C00969]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02457|molecule.C02457]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6487`

## Notes

CPD-347 + NADP -> HYDROXYPROPANAL + NADPH + PROTON; direction=REVERSIBLE
