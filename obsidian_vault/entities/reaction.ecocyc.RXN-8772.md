---
entity_id: "reaction.ecocyc.RXN-8772"
entity_type: "reaction"
name: "RXN-8772"
source_database: "EcoCyc"
source_id: "RXN-8772"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8772

`reaction.ecocyc.RXN-8772`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8772`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ARABITOL + NADP -> L-ARABINOSE + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: L-ARABITOL + NADP -> L-ARABINOSE + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: NADP+ (molecule.C00006), L-Arabitol (molecule.C00532). Products: NADPH (molecule.C00005), H+ (molecule.C00080), L-Arabinose (molecule.C00259).

## Annotation

L-ARABITOL + NADP -> L-ARABINOSE + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00532|molecule.C00532]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8772`

## Notes

L-ARABITOL + NADP -> L-ARABINOSE + NADPH + PROTON; direction=REVERSIBLE
