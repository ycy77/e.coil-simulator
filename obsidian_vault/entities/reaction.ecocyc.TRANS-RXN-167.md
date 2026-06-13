---
entity_id: "reaction.ecocyc.TRANS-RXN-167"
entity_type: "reaction"
name: "TRANS-RXN-167"
source_database: "EcoCyc"
source_id: "TRANS-RXN-167"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-167

`reaction.ecocyc.TRANS-RXN-167`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-167`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + N-acetyl-D-glucosamine -> Hpr-Histidine + N-ACETYL-D-GLUCOSAMINE-6-P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + N-acetyl-D-glucosamine -> Hpr-Histidine + N-ACETYL-D-GLUCOSAMINE-6-P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165), N-acetylglucosamine-specific PTS enzyme II (complex.ecocyc.CPLX-167). Substrates: N-Acetyl-D-glucosamine (molecule.C00140), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: N-Acetyl-D-glucosamine 6-phosphate (molecule.C00357), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + N-acetyl-D-glucosamine -> Hpr-Histidine + N-ACETYL-D-GLUCOSAMINE-6-P; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-167|complex.ecocyc.CPLX-167]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00140|molecule.C00140]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-167`

## Notes

Hpr-pi-phospho-L-histidines + N-acetyl-D-glucosamine -> Hpr-Histidine + N-ACETYL-D-GLUCOSAMINE-6-P; direction=PHYSIOL-LEFT-TO-RIGHT
