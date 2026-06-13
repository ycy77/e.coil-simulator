---
entity_id: "reaction.ecocyc.RXN-21080"
entity_type: "reaction"
name: "RXN-21080"
source_database: "EcoCyc"
source_id: "RXN-21080"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21080

`reaction.ecocyc.RXN-21080`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21080`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> Hpr-pi-phospho-L-histidines + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> Hpr-pi-phospho-L-histidines + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Phosphoenolpyruvate (molecule.C00074), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine). Products: Pyruvate (molecule.C00022), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines).

## Annotation

PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> Hpr-pi-phospho-L-histidines + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21080`

## Notes

PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> Hpr-pi-phospho-L-histidines + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
