---
entity_id: "reaction.ecocyc.PEPCARBOX-RXN"
entity_type: "reaction"
name: "PEPCARBOX-RXN"
source_database: "EcoCyc"
source_id: "PEPCARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PEPCARBOX-RXN

`reaction.ecocyc.PEPCARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PEPCARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction forms oxaloacetate, a four-carbon dicarboxylic acid source for the tricarboxylic acid cycle, under anaerobic conditions. EcoCyc reaction equation: Pi + OXALACETIC_ACID -> PHOSPHO-ENOL-PYRUVATE + HCO3; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction forms oxaloacetate, a four-carbon dicarboxylic acid source for the tricarboxylic acid cycle, under anaerobic conditions.

## Biological Role

Catalyzed by phosphoenolpyruvate carboxylase (complex.ecocyc.PEPCARBOX-CPLX). Substrates: Oxaloacetate (molecule.C00036), phosphate (molecule.ecocyc.Pi). Products: Phosphoenolpyruvate (molecule.C00074), HCO3- (molecule.C00288).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)

## Annotation

This reaction forms oxaloacetate, a four-carbon dicarboxylic acid source for the tricarboxylic acid cycle, under anaerobic conditions.

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `activates` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00112|molecule.C00112]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C02679|molecule.C02679]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1682|molecule.ecocyc.CPD0-1682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.PEPCARBOX-CPLX|complex.ecocyc.PEPCARBOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PEPCARBOX-RXN`

## Notes

Pi + OXALACETIC_ACID -> PHOSPHO-ENOL-PYRUVATE + HCO3; direction=PHYSIOL-RIGHT-TO-LEFT
