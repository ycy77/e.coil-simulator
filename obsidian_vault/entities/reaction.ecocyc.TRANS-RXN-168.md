---
entity_id: "reaction.ecocyc.TRANS-RXN-168"
entity_type: "reaction"
name: "TRANS-RXN-168"
source_database: "EcoCyc"
source_id: "TRANS-RXN-168"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-168

`reaction.ecocyc.TRANS-RXN-168`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-168`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + TREHALOSE -> TREHALOSE-6P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + TREHALOSE -> TREHALOSE-6P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by trehalose-specific PTS enzyme II (complex.ecocyc.CPLX-168). Substrates: alpha,alpha-Trehalose (molecule.C01083), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: alpha,alpha'-Trehalose 6-phosphate (molecule.C00689), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + TREHALOSE -> TREHALOSE-6P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-168|complex.ecocyc.CPLX-168]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00689|molecule.C00689]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01083|molecule.C01083]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-168`

## Notes

Hpr-pi-phospho-L-histidines + TREHALOSE -> TREHALOSE-6P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
