---
entity_id: "reaction.ecocyc.RXN0-2461"
entity_type: "reaction"
name: "RXN0-2461"
source_database: "EcoCyc"
source_id: "RXN0-2461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2461

`reaction.ecocyc.RXN0-2461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2461`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + ASCORBATE -> L-ASCORBATE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + ASCORBATE -> L-ASCORBATE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-ascorbate specific PTS enzyme II (complex.ecocyc.EIISGA). Substrates: Ascorbate (molecule.C00072), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: L-Ascorbate 6-phosphate (molecule.C16186), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Enriched Pathways

- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Annotation

Hpr-pi-phospho-L-histidines + ASCORBATE -> L-ASCORBATE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.EIISGA|complex.ecocyc.EIISGA]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C16186|molecule.C16186]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00072|molecule.C00072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2461`

## Notes

Hpr-pi-phospho-L-histidines + ASCORBATE -> L-ASCORBATE-6-PHOSPHATE + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
