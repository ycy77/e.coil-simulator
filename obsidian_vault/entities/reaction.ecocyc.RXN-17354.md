---
entity_id: "reaction.ecocyc.RXN-17354"
entity_type: "reaction"
name: "RXN-17354"
source_database: "EcoCyc"
source_id: "RXN-17354"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17354

`reaction.ecocyc.RXN-17354`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17354`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-ENOL-PYRUVATE + PTS-I-Histidines -> PYRUVATE + PTS-I-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-ENOL-PYRUVATE + PTS-I-Histidines -> PYRUVATE + PTS-I-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Phosphoenolpyruvate (molecule.C00074), a [PTS enzyme I]-L-histidine (molecule.ecocyc.PTS-I-Histidines). Products: Pyruvate (molecule.C00022), a [PTS enzyme I]-Nπ-phospho-L-histidine (molecule.ecocyc.PTS-I-pi-phospho-L-histidines).

## Annotation

PHOSPHO-ENOL-PYRUVATE + PTS-I-Histidines -> PYRUVATE + PTS-I-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PTS-I-pi-phospho-L-histidines|molecule.ecocyc.PTS-I-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PTS-I-Histidines|molecule.ecocyc.PTS-I-Histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17354`

## Notes

PHOSPHO-ENOL-PYRUVATE + PTS-I-Histidines -> PYRUVATE + PTS-I-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT
