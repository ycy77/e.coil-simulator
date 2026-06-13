---
entity_id: "reaction.ecocyc.PGLUCISOM-RXN"
entity_type: "reaction"
name: "PGLUCISOM-RXN"
source_database: "EcoCyc"
source_id: "PGLUCISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PHOSPHOGLUCOSE ISOMERASE"
  - "PHOSPHOHEXOSE ISOMERASE"
  - "PHOSPHOHEXOMUTASE"
  - "OXOISOMERASE"
  - "HEXOSEPHOSPHATE ISOMERASE"
  - "PHOSPHOSACCHAROMUTASE"
  - "PHOSPHOGLUCOISOMERASE"
  - "PHOSPHOHEXOISOMERASE"
---

# PGLUCISOM-RXN

`reaction.ecocyc.PGLUCISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PGLUCISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALPHA-GLC-6-P -> FRUCTOSE-6P; direction=REVERSIBLE EcoCyc reaction equation: ALPHA-GLC-6-P -> FRUCTOSE-6P; direction=REVERSIBLE.

## Biological Role

Catalyzed by 5-dehydro-4-deoxy-D-glucuronate isomerase (complex.ecocyc.CPLX-8401), glucose-6-phosphate isomerase (complex.ecocyc.CPLX0-7877). Substrates: alpha-D-Glucose 6-phosphate (molecule.C00668). Products: β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Annotation

ALPHA-GLC-6-P -> FRUCTOSE-6P; direction=REVERSIBLE

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX-8401|complex.ecocyc.CPLX-8401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7877|complex.ecocyc.CPLX0-7877]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00668|molecule.C00668]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PGLUCISOM-RXN`

## Notes

ALPHA-GLC-6-P -> FRUCTOSE-6P; direction=REVERSIBLE
