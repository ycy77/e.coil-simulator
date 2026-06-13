---
entity_id: "reaction.ecocyc.RXN0-7272"
entity_type: "reaction"
name: "RXN0-7272"
source_database: "EcoCyc"
source_id: "RXN0-7272"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7272

`reaction.ecocyc.RXN0-7272`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7272`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-1-PHOSPHATIDYL-ETHANOLAMINE + GLYCEROL -> L-1-PHOSPHATIDYL-GLYCEROL + ETHANOL-AMINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + GLYCEROL -> L-1-PHOSPHATIDYL-GLYCEROL + ETHANOL-AMINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by clsB (protein.P0AA84). Substrates: Glycerol (molecule.C00116), Phosphatidylethanolamine (molecule.C00350). Products: Ethanolamine (molecule.C00189), Phosphatidylglycerol (molecule.C00344).

## Annotation

L-1-PHOSPHATIDYL-ETHANOLAMINE + GLYCEROL -> L-1-PHOSPHATIDYL-GLYCEROL + ETHANOL-AMINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AA84|protein.P0AA84]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7272`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + GLYCEROL -> L-1-PHOSPHATIDYL-GLYCEROL + ETHANOL-AMINE; direction=LEFT-TO-RIGHT
