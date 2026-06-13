---
entity_id: "reaction.ecocyc.TRANS-RXN0-518"
entity_type: "reaction"
name: "TRANS-RXN0-518"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-518"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-518

`reaction.ecocyc.TRANS-RXN0-518`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-518`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-3570 + Hpr-pi-phospho-L-histidines -> CPD0-2499 + Hpr-Histidine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3570 + Hpr-pi-phospho-L-histidines -> CPD0-2499 + Hpr-Histidine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase (complex.ecocyc.CPLX-154). Substrates: methyl β-D-glucoside (molecule.ecocyc.CPD-3570), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: methyl β-D-glucoside 6-phosphate (molecule.ecocyc.CPD0-2499), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

CPD-3570 + Hpr-pi-phospho-L-histidines -> CPD0-2499 + Hpr-Histidine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-154|complex.ecocyc.CPLX-154]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2499|molecule.ecocyc.CPD0-2499]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3570|molecule.ecocyc.CPD-3570]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-518`

## Notes

CPD-3570 + Hpr-pi-phospho-L-histidines -> CPD0-2499 + Hpr-Histidine; direction=LEFT-TO-RIGHT
