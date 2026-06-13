---
entity_id: "reaction.ecocyc.IMIDPHOSDEHYD-RXN"
entity_type: "reaction"
name: "IMIDPHOSDEHYD-RXN"
source_database: "EcoCyc"
source_id: "IMIDPHOSDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# IMIDPHOSDEHYD-RXN

`reaction.ecocyc.IMIDPHOSDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:IMIDPHOSDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the seventh step of the histidine biosynthesis pathway EcoCyc reaction equation: D-ERYTHRO-IMIDAZOLE-GLYCEROL-P -> IMIDAZOLE-ACETOL-P + WATER; direction=LEFT-TO-RIGHT. This is the seventh step of the histidine biosynthesis pathway

## Biological Role

Catalyzed by imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase (complex.ecocyc.IMIDHISTID-CPLX). Substrates: D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate (molecule.C04666). Products: H2O (molecule.C00001), 3-(Imidazol-4-yl)-2-oxopropyl phosphate (molecule.C01267).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the seventh step of the histidine biosynthesis pathway

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.IMIDHISTID-CPLX|complex.ecocyc.IMIDHISTID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01267|molecule.C01267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04666|molecule.C04666]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1491|molecule.ecocyc.CPD0-1491]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:IMIDPHOSDEHYD-RXN`

## Notes

D-ERYTHRO-IMIDAZOLE-GLYCEROL-P -> IMIDAZOLE-ACETOL-P + WATER; direction=LEFT-TO-RIGHT
