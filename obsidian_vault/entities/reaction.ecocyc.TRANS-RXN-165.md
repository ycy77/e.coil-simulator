---
entity_id: "reaction.ecocyc.TRANS-RXN-165"
entity_type: "reaction"
name: "TRANS-RXN-165"
source_database: "EcoCyc"
source_id: "TRANS-RXN-165"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-165

`reaction.ecocyc.TRANS-RXN-165`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-165`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + D-mannopyranose -> CPD-15979 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + D-mannopyranose -> CPD-15979 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165). Substrates: D-mannopyranose (molecule.ecocyc.D-mannopyranose), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Enriched Pathways

- `ecocyc.MANNCAT-PWY` D-mannose degradation I (EcoCyc)

## Annotation

Hpr-pi-phospho-L-histidines + D-mannopyranose -> CPD-15979 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.MANNCAT-PWY` D-mannose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.D-mannopyranose|molecule.ecocyc.D-mannopyranose]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-165`

## Notes

Hpr-pi-phospho-L-histidines + D-mannopyranose -> CPD-15979 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
