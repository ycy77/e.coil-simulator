---
entity_id: "reaction.ecocyc.3PGAREARR-RXN"
entity_type: "reaction"
name: "3PGAREARR-RXN"
source_database: "EcoCyc"
source_id: "3PGAREARR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PHOSPHOGLYCEROMUTASE"
  - "PHOSPHOGLYCERATE PHOSPHOMUTASE"
---

# 3PGAREARR-RXN

`reaction.ecocyc.3PGAREARR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3PGAREARR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-PG -> G3P; direction=REVERSIBLE EcoCyc reaction equation: 2-PG -> G3P; direction=REVERSIBLE.

## Biological Role

Catalyzed by gpmI (protein.P37689). Substrates: 2-Phospho-D-glycerate (molecule.C00631). Products: 3-Phospho-D-glycerate (molecule.C00197).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

2-PG -> G3P; direction=REVERSIBLE

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37689|protein.P37689]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3PGAREARR-RXN`

## Notes

2-PG -> G3P; direction=REVERSIBLE
