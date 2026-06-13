---
entity_id: "reaction.ecocyc.RXN-15513"
entity_type: "reaction"
name: "RXN-15513"
source_database: "EcoCyc"
source_id: "RXN-15513"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15513

`reaction.ecocyc.RXN-15513`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15513`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-PG -> G3P; direction=REVERSIBLE EcoCyc reaction equation: 2-PG -> G3P; direction=REVERSIBLE.

## Biological Role

Catalyzed by 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase (complex.ecocyc.PHOSGLYCMUTASE). Substrates: 2-Phospho-D-glycerate (molecule.C00631). Products: 3-Phospho-D-glycerate (molecule.C00197).

## Enriched Pathways

- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

2-PG -> G3P; direction=REVERSIBLE

## Pathways

- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.PHOSGLYCMUTASE|complex.ecocyc.PHOSGLYCMUTASE]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4584|molecule.ecocyc.CPD-4584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-15513`

## Notes

2-PG -> G3P; direction=REVERSIBLE
