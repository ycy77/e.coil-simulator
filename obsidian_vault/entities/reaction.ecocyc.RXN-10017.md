---
entity_id: "reaction.ecocyc.RXN-10017"
entity_type: "reaction"
name: "RXN-10017"
source_database: "EcoCyc"
source_id: "RXN-10017"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10017

`reaction.ecocyc.RXN-10017`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10017`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10773 + WATER -> CPD-10774; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10773 + WATER -> CPD-10774; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), (2R,4S)-2-methyl-2,4-dihydroxydihydrofuran-3-one (molecule.ecocyc.CPD-10773). Products: R-THMF (molecule.C21382).

## Enriched Pathways

- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Annotation

CPD-10773 + WATER -> CPD-10774; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C21382|molecule.C21382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10773|molecule.ecocyc.CPD-10773]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10017`

## Notes

CPD-10773 + WATER -> CPD-10774; direction=LEFT-TO-RIGHT
