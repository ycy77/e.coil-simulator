---
entity_id: "reaction.ecocyc.RXN-17355"
entity_type: "reaction"
name: "RXN-17355"
source_database: "EcoCyc"
source_id: "RXN-17355"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17355

`reaction.ecocyc.RXN-17355`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17355`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PTS-I-pi-phospho-L-histidines + Hpr-Histidine -> PTS-I-Histidines + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PTS-I-pi-phospho-L-histidines + Hpr-Histidine -> PTS-I-Histidines + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine), a [PTS enzyme I]-Nπ-phospho-L-histidine (molecule.ecocyc.PTS-I-pi-phospho-L-histidines). Products: an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines), a [PTS enzyme I]-L-histidine (molecule.ecocyc.PTS-I-Histidines).

## Annotation

PTS-I-pi-phospho-L-histidines + Hpr-Histidine -> PTS-I-Histidines + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PTS-I-Histidines|molecule.ecocyc.PTS-I-Histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PTS-I-pi-phospho-L-histidines|molecule.ecocyc.PTS-I-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17355`

## Notes

PTS-I-pi-phospho-L-histidines + Hpr-Histidine -> PTS-I-Histidines + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT
