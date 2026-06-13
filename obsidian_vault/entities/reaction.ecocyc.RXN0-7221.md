---
entity_id: "reaction.ecocyc.RXN0-7221"
entity_type: "reaction"
name: "D-arabinose:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-7221"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-arabinose:proton symport

`reaction.ecocyc.RXN0-7221`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7221`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-ARABINOSE + PROTON -> D-ARABINOSE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: D-ARABINOSE + PROTON -> D-ARABINOSE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by fucP (protein.P11551). Substrates: H+ (molecule.C00080), D-Arabinose (molecule.C00216). Products: H+ (molecule.C00080), D-Arabinose (molecule.C00216).

## Annotation

D-ARABINOSE + PROTON -> D-ARABINOSE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P11551|protein.P11551]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00216|molecule.C00216]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00216|molecule.C00216]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7221`

## Notes

D-ARABINOSE + PROTON -> D-ARABINOSE + PROTON; direction=REVERSIBLE
