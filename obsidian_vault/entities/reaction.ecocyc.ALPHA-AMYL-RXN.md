---
entity_id: "reaction.ecocyc.ALPHA-AMYL-RXN"
entity_type: "reaction"
name: "ALPHA-AMYL-RXN"
source_database: "EcoCyc"
source_id: "ALPHA-AMYL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALPHA-AMYL-RXN

`reaction.ecocyc.ALPHA-AMYL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALPHA-AMYL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In general the reaction is the endohydrolysis of 1,4-α-D-glucosidic linkages in polysaccharides containing three or more 1,4-α-linked D-glucose units. EcoCyc reaction equation: 1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan; direction=PHYSIOL-LEFT-TO-RIGHT. In general the reaction is the endohydrolysis of 1,4-α-D-glucosidic linkages in polysaccharides containing three or more 1,4-α-linked D-glucose units.

## Biological Role

Catalyzed by amyA (protein.P26612). Substrates: H2O (molecule.C00001), Amylose (molecule.C00718). Products: Amylose (molecule.C00718).

## Annotation

In general the reaction is the endohydrolysis of 1,4-α-D-glucosidic linkages in polysaccharides containing three or more 1,4-α-linked D-glucose units.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P26612|protein.P26612]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALPHA-AMYL-RXN`

## Notes

1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan; direction=PHYSIOL-LEFT-TO-RIGHT
