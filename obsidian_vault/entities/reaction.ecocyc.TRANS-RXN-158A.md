---
entity_id: "reaction.ecocyc.TRANS-RXN-158A"
entity_type: "reaction"
name: "TRANS-RXN-158A"
source_database: "EcoCyc"
source_id: "TRANS-RXN-158A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-158A

`reaction.ecocyc.TRANS-RXN-158A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-158A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FRU + Hpr-pi-phospho-L-histidines -> CPD-15709 + Hpr-Histidine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FRU + Hpr-pi-phospho-L-histidines -> CPD-15709 + Hpr-Histidine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165). Substrates: D-Fructose (molecule.C00095), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: keto-D-fructose 6-phosphate (molecule.ecocyc.CPD-15709), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

FRU + Hpr-pi-phospho-L-histidines -> CPD-15709 + Hpr-Histidine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15709|molecule.ecocyc.CPD-15709]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00095|molecule.C00095]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-158A`

## Notes

FRU + Hpr-pi-phospho-L-histidines -> CPD-15709 + Hpr-Histidine; direction=LEFT-TO-RIGHT
