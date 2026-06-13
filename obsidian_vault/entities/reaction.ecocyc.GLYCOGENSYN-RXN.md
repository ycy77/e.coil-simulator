---
entity_id: "reaction.ecocyc.GLYCOGENSYN-RXN"
entity_type: "reaction"
name: "GLYCOGENSYN-RXN"
source_database: "EcoCyc"
source_id: "GLYCOGENSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOGENSYN-RXN

`reaction.ecocyc.GLYCOGENSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOGENSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in glycogen biosynthesis. EcoCyc reaction equation: 1-4-alpha-D-Glucan + ADP-D-GLUCOSE -> ADP + 1-4-alpha-D-Glucan; direction=REVERSIBLE. This is the second step in glycogen biosynthesis.

## Biological Role

Catalyzed by glgA (protein.P0A6U8). Substrates: ADP-glucose (molecule.C00498), Amylose (molecule.C00718). Products: ADP (molecule.C00008), Amylose (molecule.C00718).

## Enriched Pathways

- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)

## Annotation

This is the second step in glycogen biosynthesis.

## Pathways

- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6U8|protein.P0A6U8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCOGENSYN-RXN`

## Notes

1-4-alpha-D-Glucan + ADP-D-GLUCOSE -> ADP + 1-4-alpha-D-Glucan; direction=REVERSIBLE
