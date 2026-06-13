---
entity_id: "reaction.ecocyc.TRANS-RXN0-618"
entity_type: "reaction"
name: "Transport of D-fructopyranose"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-618"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Transport of D-fructopyranose

`reaction.ecocyc.TRANS-RXN0-618`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-618`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PTS-I-pi-phospho-L-histidines + D-Fructopyranose -> PTS-I-Histidines + D-fructopyranose-1-phosphate; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PTS-I-pi-phospho-L-histidines + D-Fructopyranose -> PTS-I-Histidines + D-fructopyranose-1-phosphate; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fructose-specific PTS enzyme II (complex.ecocyc.CPLX-158). Substrates: D-fructopyranose (molecule.ecocyc.D-Fructopyranose), a [PTS enzyme I]-Nπ-phospho-L-histidine (molecule.ecocyc.PTS-I-pi-phospho-L-histidines). Products: D-fructopyranose 1-phosphate (molecule.ecocyc.D-fructopyranose-1-phosphate), a [PTS enzyme I]-L-histidine (molecule.ecocyc.PTS-I-Histidines).

## Annotation

PTS-I-pi-phospho-L-histidines + D-Fructopyranose -> PTS-I-Histidines + D-fructopyranose-1-phosphate; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-158|complex.ecocyc.CPLX-158]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.D-fructopyranose-1-phosphate|molecule.ecocyc.D-fructopyranose-1-phosphate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PTS-I-Histidines|molecule.ecocyc.PTS-I-Histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.D-Fructopyranose|molecule.ecocyc.D-Fructopyranose]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PTS-I-pi-phospho-L-histidines|molecule.ecocyc.PTS-I-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-618`

## Notes

PTS-I-pi-phospho-L-histidines + D-Fructopyranose -> PTS-I-Histidines + D-fructopyranose-1-phosphate; direction=PHYSIOL-LEFT-TO-RIGHT
