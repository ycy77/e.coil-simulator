---
entity_id: "reaction.ecocyc.FUCULOKIN-RXN"
entity_type: "reaction"
name: "FUCULOKIN-RXN"
source_database: "EcoCyc"
source_id: "FUCULOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FUCULOKIN-RXN

`reaction.ecocyc.FUCULOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FUCULOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step in fucose catabolism. EcoCyc reaction equation: L-FUCULOSE + ATP -> PROTON + FUCULOSE-1P + ADP; direction=LEFT-TO-RIGHT. The second step in fucose catabolism.

## Biological Role

Catalyzed by fucK (protein.P11553). Substrates: ATP (molecule.C00002), L-Fuculose (molecule.C01721). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Fuculose 1-phosphate (molecule.C01099).

## Enriched Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Annotation

The second step in fucose catabolism.

## Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P11553|protein.P11553]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01099|molecule.C01099]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01721|molecule.C01721]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FUCULOKIN-RXN`

## Notes

L-FUCULOSE + ATP -> PROTON + FUCULOSE-1P + ADP; direction=LEFT-TO-RIGHT
