---
entity_id: "reaction.ecocyc.RXN-16009"
entity_type: "reaction"
name: "RXN-16009"
source_database: "EcoCyc"
source_id: "RXN-16009"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16009

`reaction.ecocyc.RXN-16009`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16009`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleoside-3-5-bisphosphate + WATER -> Nucleoside-Monophosphates + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Nucleoside-3-5-bisphosphate + WATER -> Nucleoside-Monophosphates + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rnm (protein.P77766). Substrates: H2O (molecule.C00001), a nucleoside 3',5'-bisphosphate (molecule.ecocyc.Nucleoside-3-5-bisphosphate). Products: a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates), phosphate (molecule.ecocyc.Pi).

## Annotation

Nucleoside-3-5-bisphosphate + WATER -> Nucleoside-Monophosphates + Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77766|protein.P77766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleoside-3-5-bisphosphate|molecule.ecocyc.Nucleoside-3-5-bisphosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16009`

## Notes

Nucleoside-3-5-bisphosphate + WATER -> Nucleoside-Monophosphates + Pi; direction=LEFT-TO-RIGHT
