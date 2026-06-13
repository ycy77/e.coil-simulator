---
entity_id: "reaction.ecocyc.RXN0-7012"
entity_type: "reaction"
name: "RXN0-7012"
source_database: "EcoCyc"
source_id: "RXN0-7012"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7012

`reaction.ecocyc.RXN0-7012`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7012`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-1-PHOSPHATIDYL-GLYCEROL + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CARDIOLIPIN + ETHANOL-AMINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-GLYCEROL + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CARDIOLIPIN + ETHANOL-AMINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by clsC (protein.P75919). Substrates: Phosphatidylglycerol (molecule.C00344), Phosphatidylethanolamine (molecule.C00350). Products: Ethanolamine (molecule.C00189), Cardiolipin (molecule.C05980).

## Enriched Pathways

- `ecocyc.PWY0-1545` cardiolipin biosynthesis III (EcoCyc)

## Annotation

L-1-PHOSPHATIDYL-GLYCEROL + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CARDIOLIPIN + ETHANOL-AMINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1545` cardiolipin biosynthesis III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75919|protein.P75919]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7012`

## Notes

L-1-PHOSPHATIDYL-GLYCEROL + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CARDIOLIPIN + ETHANOL-AMINE; direction=LEFT-TO-RIGHT
