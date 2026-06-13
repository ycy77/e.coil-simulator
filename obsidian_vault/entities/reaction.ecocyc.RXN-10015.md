---
entity_id: "reaction.ecocyc.RXN-10015"
entity_type: "reaction"
name: "RXN-10015"
source_database: "EcoCyc"
source_id: "RXN-10015"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10015

`reaction.ecocyc.RXN-10015`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10015`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXYPENTANEDIONE -> CPD-10773; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXYPENTANEDIONE -> CPD-10773; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: (4S)-4,5-dihydroxypentane-2,3-dione (molecule.ecocyc.DIHYDROXYPENTANEDIONE). Products: (2R,4S)-2-methyl-2,4-dihydroxydihydrofuran-3-one (molecule.ecocyc.CPD-10773).

## Enriched Pathways

- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Annotation

DIHYDROXYPENTANEDIONE -> CPD-10773; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-10773|molecule.ecocyc.CPD-10773]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.DIHYDROXYPENTANEDIONE|molecule.ecocyc.DIHYDROXYPENTANEDIONE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10015`

## Notes

DIHYDROXYPENTANEDIONE -> CPD-10773; direction=LEFT-TO-RIGHT
