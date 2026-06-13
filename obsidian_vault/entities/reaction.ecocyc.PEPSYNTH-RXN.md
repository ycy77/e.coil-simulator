---
entity_id: "reaction.ecocyc.PEPSYNTH-RXN"
entity_type: "reaction"
name: "PEPSYNTH-RXN"
source_database: "EcoCyc"
source_id: "PEPSYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PEPSYNTH-RXN

`reaction.ecocyc.PEPSYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PEPSYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction of gluconeogenesis. EcoCyc reaction equation: WATER + PYRUVATE + ATP -> PROTON + Pi + PHOSPHO-ENOL-PYRUVATE + AMP; direction=REVERSIBLE. A reaction of gluconeogenesis.

## Biological Role

Catalyzed by phosphoenolpyruvate synthetase (complex.ecocyc.PEPSYNTH-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Pyruvate (molecule.C00022). Products: AMP (molecule.C00020), Phosphoenolpyruvate (molecule.C00074), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

A reaction of gluconeogenesis.

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.PEPSYNTH-CPLX|complex.ecocyc.PEPSYNTH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PEPSYNTH-RXN`

## Notes

WATER + PYRUVATE + ATP -> PROTON + Pi + PHOSPHO-ENOL-PYRUVATE + AMP; direction=REVERSIBLE
