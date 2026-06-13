---
entity_id: "reaction.ecocyc.RIBOFLAVINKIN-RXN"
entity_type: "reaction"
name: "RIBOFLAVINKIN-RXN"
source_database: "EcoCyc"
source_id: "RIBOFLAVINKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOFLAVINKIN-RXN

`reaction.ecocyc.RIBOFLAVINKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOFLAVINKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction produces the coenzyme FMN from riboflavin. EcoCyc reaction equation: RIBOFLAVIN + ATP -> PROTON + FMN + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction produces the coenzyme FMN from riboflavin.

## Biological Role

Catalyzed by ribF (protein.P0AG40). Substrates: ATP (molecule.C00002), Riboflavin (molecule.C00255). Products: ADP (molecule.C00008), FMN (molecule.C00061), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

This reaction produces the coenzyme FMN from riboflavin.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AG40|protein.P0AG40]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00255|molecule.C00255]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOFLAVINKIN-RXN`

## Notes

RIBOFLAVIN + ATP -> PROTON + FMN + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
