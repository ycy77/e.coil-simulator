---
entity_id: "reaction.ecocyc.RXN-15890"
entity_type: "reaction"
name: "RXN-15890"
source_database: "EcoCyc"
source_id: "RXN-15890"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15890

`reaction.ecocyc.RXN-15890`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15890`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Holo-EntF + SERYL-AMP -> Seryl-EntF + AMP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Holo-EntF + SERYL-AMP -> Seryl-EntF + AMP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-seryl)adenylate (molecule.ecocyc.SERYL-AMP). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

Holo-EntF + SERYL-AMP -> Seryl-EntF + AMP + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.SERYL-AMP|molecule.ecocyc.SERYL-AMP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15890`

## Notes

Holo-EntF + SERYL-AMP -> Seryl-EntF + AMP + PROTON; direction=LEFT-TO-RIGHT
