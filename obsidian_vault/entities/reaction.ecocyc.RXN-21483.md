---
entity_id: "reaction.ecocyc.RXN-21483"
entity_type: "reaction"
name: "RXN-21483"
source_database: "EcoCyc"
source_id: "RXN-21483"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21483

`reaction.ecocyc.RXN-21483`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21483`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinones + PROTOPORPHYRINOGEN -> Ubiquinols + PROTOPORPHYRIN_IX; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinones + PROTOPORPHYRINOGEN -> Ubiquinols + PROTOPORPHYRIN_IX; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protoporphyrinogen oxidase (complex.ecocyc.CPLX0-7811). Substrates: Protoporphyrinogen IX (molecule.C01079), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: Ubiquinol (molecule.C00390), Protoporphyrin (molecule.C02191).

## Enriched Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)

## Annotation

Ubiquinones + PROTOPORPHYRINOGEN -> Ubiquinols + PROTOPORPHYRIN_IX; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7811|complex.ecocyc.CPLX0-7811]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02191|molecule.C02191]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01079|molecule.C01079]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21483`

## Notes

Ubiquinones + PROTOPORPHYRINOGEN -> Ubiquinols + PROTOPORPHYRIN_IX; direction=LEFT-TO-RIGHT
