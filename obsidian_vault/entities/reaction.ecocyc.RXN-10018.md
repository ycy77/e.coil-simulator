---
entity_id: "reaction.ecocyc.RXN-10018"
entity_type: "reaction"
name: "RXN-10018"
source_database: "EcoCyc"
source_id: "RXN-10018"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10018

`reaction.ecocyc.RXN-10018`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10018`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10775 + WATER -> CPD-10776; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10775 + WATER -> CPD-10776; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), (2S,4S)-2-methyl-2,4-dihydroxydihydrofuran-3-one (molecule.ecocyc.CPD-10775). Products: (2S,4S)-2-methyl-2,3,3,4-tetrahydroxytetrahydrofuran (molecule.ecocyc.CPD-10776).

## Annotation

CPD-10775 + WATER -> CPD-10776; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-10776|molecule.ecocyc.CPD-10776]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10775|molecule.ecocyc.CPD-10775]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10018`

## Notes

CPD-10775 + WATER -> CPD-10776; direction=LEFT-TO-RIGHT
