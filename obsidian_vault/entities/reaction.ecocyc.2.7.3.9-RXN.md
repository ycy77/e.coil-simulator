---
entity_id: "reaction.ecocyc.2.7.3.9-RXN"
entity_type: "reaction"
name: "2.7.3.9-RXN"
source_database: "EcoCyc"
source_id: "2.7.3.9-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.7.3.9-RXN

`reaction.ecocyc.2.7.3.9-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.3.9-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> PYRUVATE + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> PYRUVATE + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by PTS enzyme I (complex.ecocyc.CPLX0-7938). Substrates: Phosphoenolpyruvate (molecule.C00074), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine). Products: Pyruvate (molecule.C00022), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines).

## Annotation

PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> PYRUVATE + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7938|complex.ecocyc.CPLX0-7938]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.7.3.9-RXN`

## Notes

PHOSPHO-ENOL-PYRUVATE + Hpr-Histidine -> PYRUVATE + Hpr-pi-phospho-L-histidines; direction=PHYSIOL-LEFT-TO-RIGHT
