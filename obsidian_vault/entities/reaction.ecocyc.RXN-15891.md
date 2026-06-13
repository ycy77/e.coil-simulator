---
entity_id: "reaction.ecocyc.RXN-15891"
entity_type: "reaction"
name: "RXN-15891"
source_database: "EcoCyc"
source_id: "RXN-15891"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15891

`reaction.ecocyc.RXN-15891`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15891`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

23DHB-EntB + Seryl-EntF -> Holo-EntB + DHB-Seryl-EntF + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 23DHB-EntB + Seryl-EntF -> Holo-EntB + DHB-Seryl-EntF + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by entF (protein.P11454). Products: H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Annotation

23DHB-EntB + Seryl-EntF -> Holo-EntB + DHB-Seryl-EntF + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.ENTBACSYN-PWY` enterobactin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P11454|protein.P11454]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-15891`

## Notes

23DHB-EntB + Seryl-EntF -> Holo-EntB + DHB-Seryl-EntF + PROTON; direction=LEFT-TO-RIGHT
