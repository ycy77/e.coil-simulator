---
entity_id: "reaction.ecocyc.TRANS-RXN-155B"
entity_type: "reaction"
name: "transport of chitobiose"
source_database: "EcoCyc"
source_id: "TRANS-RXN-155B"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# transport of chitobiose

`reaction.ecocyc.TRANS-RXN-155B`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-155B`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + CHITOBIOSE -> DIACETYLCHITOBIOSE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + CHITOBIOSE -> DIACETYLCHITOBIOSE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by N,N'-diacetylchitobiose-specific PTS enzyme II (complex.ecocyc.CPLX-155). Substrates: Chitobiose (molecule.C01674), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: N,N'-Diacetylchitobiose 6'-phosphate (molecule.C21152), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Enriched Pathways

- `ecocyc.PWY0-1309` chitobiose degradation (EcoCyc)

## Annotation

Hpr-pi-phospho-L-histidines + CHITOBIOSE -> DIACETYLCHITOBIOSE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1309` chitobiose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-155|complex.ecocyc.CPLX-155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C21152|molecule.C21152]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01674|molecule.C01674]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-155B`

## Notes

Hpr-pi-phospho-L-histidines + CHITOBIOSE -> DIACETYLCHITOBIOSE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
