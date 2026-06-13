---
entity_id: "reaction.ecocyc.LACTALDDEHYDROG-RXN"
entity_type: "reaction"
name: "LACTALDDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "LACTALDDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LACTALDDEHYDROG-RXN

`reaction.ecocyc.LACTALDDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LACTALDDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxidation of lactaldehyde. EcoCyc reaction equation: WATER + NAD + LACTALD -> PROTON + NADH + L-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT. Oxidation of lactaldehyde.

## Biological Role

Catalyzed by aldehyde dehydrogenase A, NAD-linked (complex.ecocyc.ALD-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), (S)-Lactaldehyde (molecule.C00424). Products: NADH (molecule.C00004), H+ (molecule.C00080), (S)-Lactate (molecule.C00186).

## Enriched Pathways

- `ecocyc.PWY0-1317` L-lactaldehyde degradation (aerobic) (EcoCyc)

## Annotation

Oxidation of lactaldehyde.

## Pathways

- `ecocyc.PWY0-1317` L-lactaldehyde degradation (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.ecocyc.Sulfhydryl-Groups|molecule.ecocyc.Sulfhydryl-Groups]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ALD-CPLX|complex.ecocyc.ALD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LACTALDDEHYDROG-RXN`

## Notes

WATER + NAD + LACTALD -> PROTON + NADH + L-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT
