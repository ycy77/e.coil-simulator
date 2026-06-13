---
entity_id: "reaction.ecocyc.TRANS-RXN-169"
entity_type: "reaction"
name: "TRANS-RXN-169"
source_database: "EcoCyc"
source_id: "TRANS-RXN-169"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-169

`reaction.ecocyc.TRANS-RXN-169`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-169`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + SORBITOL -> D-SORBITOL-6-P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + SORBITOL -> D-SORBITOL-6-P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannitol-specific PTS enzyme II (complex.ecocyc.CPLX-166), sorbitol-specific PTS enzyme II (complex.ecocyc.CPLX-169), galactitol-specific PTS enzyme II (complex.ecocyc.CPLX0-231). Substrates: D-Sorbitol (molecule.C00794), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: Sorbitol 6-phosphate (molecule.C01096), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + SORBITOL -> D-SORBITOL-6-P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX-166|complex.ecocyc.CPLX-166]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-169|complex.ecocyc.CPLX-169]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-231|complex.ecocyc.CPLX0-231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01096|molecule.C01096]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00794|molecule.C00794]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-169`

## Notes

Hpr-pi-phospho-L-histidines + SORBITOL -> D-SORBITOL-6-P + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
