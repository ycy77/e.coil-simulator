---
entity_id: "reaction.ecocyc.PRIBFAICARPISOM-RXN"
entity_type: "reaction"
name: "PRIBFAICARPISOM-RXN"
source_database: "EcoCyc"
source_id: "PRIBFAICARPISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PRIBFAICARPISOM-RXN

`reaction.ecocyc.PRIBFAICARPISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRIBFAICARPISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in the histidine pathway EcoCyc reaction equation: PHOSPHORIBOSYL-FORMIMINO-AICAR-P -> PHOSPHORIBULOSYL-FORMIMINO-AICAR-P; direction=LEFT-TO-RIGHT. This is the fourth step in the histidine pathway

## Biological Role

Catalyzed by hisA (protein.P10371). Substrates: 5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide (molecule.C04896). Products: N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide (molecule.C04916).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the fourth step in the histidine pathway

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P10371|protein.P10371]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04916|molecule.C04916]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04896|molecule.C04896]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PRIBFAICARPISOM-RXN`

## Notes

PHOSPHORIBOSYL-FORMIMINO-AICAR-P -> PHOSPHORIBULOSYL-FORMIMINO-AICAR-P; direction=LEFT-TO-RIGHT
