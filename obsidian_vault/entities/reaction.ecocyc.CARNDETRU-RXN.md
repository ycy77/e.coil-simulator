---
entity_id: "reaction.ecocyc.CARNDETRU-RXN"
entity_type: "reaction"
name: "CARNDETRU-RXN"
source_database: "EcoCyc"
source_id: "CARNDETRU-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CARNDETRU-RXN

`reaction.ecocyc.CARNDETRU-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CARNDETRU-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-CARNITINYL-COA -> CROTONOBETAINYL-COA + WATER; direction=REVERSIBLE EcoCyc reaction equation: L-CARNITINYL-COA -> CROTONOBETAINYL-COA + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by caiD (protein.P31551). Substrates: (R)-carnitinyl-CoA (molecule.ecocyc.L-CARNITINYL-COA). Products: H2O (molecule.C00001), crotonobetainyl-CoA (molecule.ecocyc.CROTONOBETAINYL-COA).

## Enriched Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Annotation

L-CARNITINYL-COA -> CROTONOBETAINYL-COA + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P31551|protein.P31551]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CROTONOBETAINYL-COA|molecule.ecocyc.CROTONOBETAINYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-CARNITINYL-COA|molecule.ecocyc.L-CARNITINYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CARNDETRU-RXN`

## Notes

L-CARNITINYL-COA -> CROTONOBETAINYL-COA + WATER; direction=REVERSIBLE
