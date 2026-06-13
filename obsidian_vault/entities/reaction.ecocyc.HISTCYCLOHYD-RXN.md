---
entity_id: "reaction.ecocyc.HISTCYCLOHYD-RXN"
entity_type: "reaction"
name: "HISTCYCLOHYD-RXN"
source_database: "EcoCyc"
source_id: "HISTCYCLOHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HISTCYCLOHYD-RXN

`reaction.ecocyc.HISTCYCLOHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HISTCYCLOHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the third step in the biosynthesis of histidine EcoCyc reaction equation: PHOSPHORIBOSYL-AMP + WATER -> PHOSPHORIBOSYL-FORMIMINO-AICAR-P; direction=LEFT-TO-RIGHT. This reaction is the third step in the biosynthesis of histidine

## Biological Role

Catalyzed by hisI (protein.P06989). Substrates: H2O (molecule.C00001), Phosphoribosyl-AMP (molecule.C02741). Products: 5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide (molecule.C04896).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This reaction is the third step in the biosynthesis of histidine

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P06989|protein.P06989]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04896|molecule.C04896]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02741|molecule.C02741]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HISTCYCLOHYD-RXN`

## Notes

PHOSPHORIBOSYL-AMP + WATER -> PHOSPHORIBOSYL-FORMIMINO-AICAR-P; direction=LEFT-TO-RIGHT
