---
entity_id: "reaction.ecocyc.RXN-15348"
entity_type: "reaction"
name: "RXN-15348"
source_database: "EcoCyc"
source_id: "RXN-15348"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15348

`reaction.ecocyc.RXN-15348`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15348`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-11281 + GLUTATHIONE -> HS + OXIDIZED-GLUTATHIONE; direction=REVERSIBLE EcoCyc reaction equation: CPD-11281 + GLUTATHIONE -> HS + OXIDIZED-GLUTATHIONE; direction=REVERSIBLE.

## Biological Role

Substrates: Glutathione (molecule.C00051), S-Sulfanylglutathione (molecule.C17267). Products: Glutathione disulfide (molecule.C00127), Hydrogen sulfide (molecule.C00283).

## Annotation

CPD-11281 + GLUTATHIONE -> HS + OXIDIZED-GLUTATHIONE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C17267|molecule.C17267]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15348`

## Notes

CPD-11281 + GLUTATHIONE -> HS + OXIDIZED-GLUTATHIONE; direction=REVERSIBLE
