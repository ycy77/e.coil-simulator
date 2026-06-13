---
entity_id: "reaction.ecocyc.TRANS-RXN-155"
entity_type: "reaction"
name: "TRANS-RXN-155"
source_database: "EcoCyc"
source_id: "TRANS-RXN-155"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-155

`reaction.ecocyc.TRANS-RXN-155`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-155`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + CELLOBIOSE -> CPD-507 + Hpr-Histidine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + CELLOBIOSE -> CPD-507 + Hpr-Histidine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-glucoside specific PTS enzyme II (complex.ecocyc.CPLX-153), N,N'-diacetylchitobiose-specific PTS enzyme II (complex.ecocyc.CPLX-155). Substrates: β-D-cellobiose (molecule.ecocyc.CELLOBIOSE), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: 6-Phospho-beta-D-glucosyl-(1,4)-D-glucose (molecule.C04534), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + CELLOBIOSE -> CPD-507 + Hpr-Histidine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX-153|complex.ecocyc.CPLX-153]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-155|complex.ecocyc.CPLX-155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04534|molecule.C04534]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CELLOBIOSE|molecule.ecocyc.CELLOBIOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-155`

## Notes

Hpr-pi-phospho-L-histidines + CELLOBIOSE -> CPD-507 + Hpr-Histidine; direction=LEFT-TO-RIGHT
