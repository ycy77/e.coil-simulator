---
entity_id: "reaction.ecocyc.TRANS-RXN-1567"
entity_type: "reaction"
name: "TRANS-RXN-1567"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1567"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-1567

`reaction.ecocyc.TRANS-RXN-1567`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1567`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FRU + PTS-I-pi-phospho-L-histidines -> D-fructose-1-phosphate + PTS-I-Histidines; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FRU + PTS-I-pi-phospho-L-histidines -> D-fructose-1-phosphate + PTS-I-Histidines; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fructose-specific PTS enzyme II (complex.ecocyc.CPLX-158). Substrates: D-Fructose (molecule.C00095), a [PTS enzyme I]-Nπ-phospho-L-histidine (molecule.ecocyc.PTS-I-pi-phospho-L-histidines). Products: D-Fructose 1-phosphate (molecule.C01094), a [PTS enzyme I]-L-histidine (molecule.ecocyc.PTS-I-Histidines).

## Annotation

FRU + PTS-I-pi-phospho-L-histidines -> D-fructose-1-phosphate + PTS-I-Histidines; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-158|complex.ecocyc.CPLX-158]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01094|molecule.C01094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PTS-I-Histidines|molecule.ecocyc.PTS-I-Histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00095|molecule.C00095]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PTS-I-pi-phospho-L-histidines|molecule.ecocyc.PTS-I-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-1567`

## Notes

FRU + PTS-I-pi-phospho-L-histidines -> D-fructose-1-phosphate + PTS-I-Histidines; direction=LEFT-TO-RIGHT
