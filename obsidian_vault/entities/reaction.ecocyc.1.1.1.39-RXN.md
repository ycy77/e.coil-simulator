---
entity_id: "reaction.ecocyc.1.1.1.39-RXN"
entity_type: "reaction"
name: "1.1.1.39-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.39-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.39-RXN

`reaction.ecocyc.1.1.1.39-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.39-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction of the gluconeogenesis pathway. EcoCyc reaction equation: NAD + MAL -> NADH + CARBON-DIOXIDE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction of the gluconeogenesis pathway.

## Biological Role

Catalyzed by malate dehydrogenase (oxaloacetate-decarboxylating) (complex.ecocyc.MALIC-NAD-CPLX). Substrates: NAD+ (molecule.C00003), (S)-Malate (molecule.C00149). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Pyruvate (molecule.C00022).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)

## Annotation

A reaction of the gluconeogenesis pathway.

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.MALIC-NAD-CPLX|complex.ecocyc.MALIC-NAD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1.1.1.39-RXN`

## Notes

NAD + MAL -> NADH + CARBON-DIOXIDE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
