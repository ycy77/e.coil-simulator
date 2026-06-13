---
entity_id: "reaction.ecocyc.6PFRUCTPHOS-RXN"
entity_type: "reaction"
name: "6PFRUCTPHOS-RXN"
source_database: "EcoCyc"
source_id: "6PFRUCTPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "fructose-6-phosphate phosphorylation"
---

# 6PFRUCTPHOS-RXN

`reaction.ecocyc.6PFRUCTPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:6PFRUCTPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a key control step in glycolysis EcoCyc reaction equation: FRUCTOSE-6P + ATP -> PROTON + ADP + FRUCTOSE-16-DIPHOSPHATE; direction=LEFT-TO-RIGHT. This is a key control step in glycolysis

## Biological Role

Catalyzed by 6-phosphofructokinase 1 (complex.ecocyc.6PFK-1-CPX), 6-phosphofructokinase 2 (complex.ecocyc.6PFK-2-CPX). Substrates: ATP (molecule.C00002), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Fructose 1,6-bisphosphate (molecule.C00354).

## Enriched Pathways

- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

This is a key control step in glycolysis

## Pathways

- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `activates` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0AA04|protein.P0AA04]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.6PFK-1-CPX|complex.ecocyc.6PFK-1-CPX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.6PFK-2-CPX|complex.ecocyc.6PFK-2-CPX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:6PFRUCTPHOS-RXN`

## Notes

FRUCTOSE-6P + ATP -> PROTON + ADP + FRUCTOSE-16-DIPHOSPHATE; direction=LEFT-TO-RIGHT
