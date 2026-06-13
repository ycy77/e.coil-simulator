---
entity_id: "reaction.ecocyc.RXN-19020"
entity_type: "reaction"
name: "RXN-19020"
source_database: "EcoCyc"
source_id: "RXN-19020"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19020

`reaction.ecocyc.RXN-19020`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19020`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + HYDROGEN-PEROXIDE -> Menaquinones + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinols + HYDROGEN-PEROXIDE -> Menaquinones + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ccp (protein.P37197). Substrates: Hydrogen peroxide (molecule.C00027), Menaquinol (molecule.C05819). Products: H2O (molecule.C00001), Menaquinone (molecule.C00828).

## Enriched Pathways

- `ecocyc.PWY0-1590` NADH to hydrogen peroxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1591` glycerol-3-phosphate to hydrogen peroxide electron transport (EcoCyc)

## Annotation

Menaquinols + HYDROGEN-PEROXIDE -> Menaquinones + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1590` NADH to hydrogen peroxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1591` glycerol-3-phosphate to hydrogen peroxide electron transport (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37197|protein.P37197]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19020`

## Notes

Menaquinols + HYDROGEN-PEROXIDE -> Menaquinones + WATER; direction=LEFT-TO-RIGHT
