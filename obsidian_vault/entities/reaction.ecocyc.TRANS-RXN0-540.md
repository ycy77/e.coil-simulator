---
entity_id: "reaction.ecocyc.TRANS-RXN0-540"
entity_type: "reaction"
name: "TRANS-RXN0-540"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-540"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-540

`reaction.ecocyc.TRANS-RXN0-540`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-540`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + 2-DEOXY-D-GLUCOSE -> Hpr-Histidine + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + 2-DEOXY-D-GLUCOSE -> Hpr-Histidine + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165). Substrates: 2-deoxy-D-glucose (molecule.ecocyc.2-DEOXY-D-GLUCOSE), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: 2-deoxy-D-glucose 6-phosphate (molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + 2-DEOXY-D-GLUCOSE -> Hpr-Histidine + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE|molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.2-DEOXY-D-GLUCOSE|molecule.ecocyc.2-DEOXY-D-GLUCOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-540`

## Notes

Hpr-pi-phospho-L-histidines + 2-DEOXY-D-GLUCOSE -> Hpr-Histidine + 2-DEOXY-D-GLUCOSE-6-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
