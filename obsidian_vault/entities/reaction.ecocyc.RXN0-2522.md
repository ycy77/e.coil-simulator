---
entity_id: "reaction.ecocyc.RXN0-2522"
entity_type: "reaction"
name: "RXN0-2522"
source_database: "EcoCyc"
source_id: "RXN0-2522"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2522

`reaction.ecocyc.RXN0-2522`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2522`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + 2-O-ALPHA-MANNOSYL-D-GLYCERATE -> CPD0-1063 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + 2-O-ALPHA-MANNOSYL-D-GLYCERATE -> CPD0-1063 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mngA (protein.P54745). Substrates: 2-O-(alpha-D-Mannosyl)-D-glycerate (molecule.C11544), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: 2-O-(6-Phospho-alpha-mannosyl)-D-glycerate (molecule.C16699), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Annotation

Hpr-pi-phospho-L-histidines + 2-O-ALPHA-MANNOSYL-D-GLYCERATE -> CPD0-1063 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P54745|protein.P54745]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C16699|molecule.C16699]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11544|molecule.C11544]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2522`

## Notes

Hpr-pi-phospho-L-histidines + 2-O-ALPHA-MANNOSYL-D-GLYCERATE -> CPD0-1063 + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
