---
entity_id: "reaction.ecocyc.TRANS-RXN-153A"
entity_type: "reaction"
name: "TRANS-RXN-153A"
source_database: "EcoCyc"
source_id: "TRANS-RXN-153A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-153A

`reaction.ecocyc.TRANS-RXN-153A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-153A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + CPD-1142 -> CPD-1181 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + CPD-1142 -> CPD-1181 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-glucoside specific PTS enzyme II (complex.ecocyc.CPLX-153), β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase (complex.ecocyc.CPLX-154). Substrates: Salicin (molecule.C01451), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: Salicin 6-phosphate (molecule.C06188), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + CPD-1142 -> CPD-1181 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX-153|complex.ecocyc.CPLX-153]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-154|complex.ecocyc.CPLX-154]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06188|molecule.C06188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01451|molecule.C01451]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-153A`

## Notes

Hpr-pi-phospho-L-histidines + CPD-1142 -> CPD-1181 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
