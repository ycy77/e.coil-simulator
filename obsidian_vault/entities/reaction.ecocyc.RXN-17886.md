---
entity_id: "reaction.ecocyc.RXN-17886"
entity_type: "reaction"
name: "RXN-17886"
source_database: "EcoCyc"
source_id: "RXN-17886"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17886

`reaction.ecocyc.RXN-17886`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17886`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19217 + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + HYDROXYLAMINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-19217 + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + HYDROXYLAMINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), S-(hydroxysulfenamide)glutathione (molecule.ecocyc.CPD-19217). Products: Glutathione disulfide (molecule.C00127), Hydroxylamine (molecule.C00192).

## Annotation

CPD-19217 + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + HYDROXYLAMINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19217|molecule.ecocyc.CPD-19217]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17886`

## Notes

CPD-19217 + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + HYDROXYLAMINE; direction=PHYSIOL-LEFT-TO-RIGHT
