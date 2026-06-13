---
entity_id: "reaction.ecocyc.PHOSGLYPHOS-RXN"
entity_type: "reaction"
name: "PHOSGLYPHOS-RXN"
source_database: "EcoCyc"
source_id: "PHOSGLYPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSGLYPHOS-RXN

`reaction.ecocyc.PHOSGLYPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSGLYPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction a phosphoryl group is transferred from the acyl phosphate of 1,3 diphosphoglycerate to ADP thereby forming ATP and 3-phosphoglycerate. EcoCyc reaction equation: G3P + ATP -> DPG + ADP; direction=REVERSIBLE. In this reaction a phosphoryl group is transferred from the acyl phosphate of 1,3 diphosphoglycerate to ADP thereby forming ATP and 3-phosphoglycerate.

## Biological Role

Catalyzed by pgk (protein.P0A799). Substrates: ATP (molecule.C00002), 3-Phospho-D-glycerate (molecule.C00197). Products: ADP (molecule.C00008), 3-Phospho-D-glyceroyl phosphate (molecule.C00236).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

In this reaction a phosphoryl group is transferred from the acyl phosphate of 1,3 diphosphoglycerate to ADP thereby forming ATP and 3-phosphoglycerate.

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A799|protein.P0A799]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00236|molecule.C00236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOSGLYPHOS-RXN`

## Notes

G3P + ATP -> DPG + ADP; direction=REVERSIBLE
