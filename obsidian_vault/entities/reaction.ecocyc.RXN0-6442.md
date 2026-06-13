---
entity_id: "reaction.ecocyc.RXN0-6442"
entity_type: "reaction"
name: "RXN0-6442"
source_database: "EcoCyc"
source_id: "RXN0-6442"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6442

`reaction.ecocyc.RXN0-6442`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6442`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-62 + Holo-EntB -> 23DHB-EntB + AMP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-62 + Holo-EntB -> 23DHB-EntB + AMP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: (2,3-dihydroxybenzoyl)adenylate (molecule.ecocyc.CPD-62). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

CPD-62 + Holo-EntB -> 23DHB-EntB + AMP + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-62|molecule.ecocyc.CPD-62]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6442`

## Notes

CPD-62 + Holo-EntB -> 23DHB-EntB + AMP + PROTON; direction=LEFT-TO-RIGHT
