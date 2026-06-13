---
entity_id: "reaction.ecocyc.2PGADEHYDRAT-RXN"
entity_type: "reaction"
name: "2PGADEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "2PGADEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2-PHOSPHOGLYCERATE DEHYDRATASE"
  - "ENOLASE"
---

# 2PGADEHYDRAT-RXN

`reaction.ecocyc.2PGADEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2PGADEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-PG -> PHOSPHO-ENOL-PYRUVATE + WATER; direction=REVERSIBLE EcoCyc reaction equation: 2-PG -> PHOSPHO-ENOL-PYRUVATE + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by enolase (complex.ecocyc.ENOLASE-CPLX). Substrates: 2-Phospho-D-glycerate (molecule.C00631). Products: H2O (molecule.C00001), Phosphoenolpyruvate (molecule.C00074).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

2-PG -> PHOSPHO-ENOL-PYRUVATE + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ENOLASE-CPLX|complex.ecocyc.ENOLASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2PGADEHYDRAT-RXN`

## Notes

2-PG -> PHOSPHO-ENOL-PYRUVATE + WATER; direction=REVERSIBLE
