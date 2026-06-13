---
entity_id: "reaction.ecocyc.MALIC-NADP-RXN"
entity_type: "reaction"
name: "MALIC-NADP-RXN"
source_database: "EcoCyc"
source_id: "MALIC-NADP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALIC-NADP-RXN

`reaction.ecocyc.MALIC-NADP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALIC-NADP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction supplies pyruvate when the supply of C4 compounds is abundant. EcoCyc reaction equation: NADP + MAL -> NADPH + CARBON-DIOXIDE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction supplies pyruvate when the supply of C4 compounds is abundant.

## Biological Role

Catalyzed by malate dehydrogenase (oxaloacetate-decarboxylating) (NADP+) (complex.ecocyc.MALIC-NADP-CPLX). Substrates: NADP+ (molecule.C00006), (S)-Malate (molecule.C00149). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), Pyruvate (molecule.C00022).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)

## Annotation

This reaction supplies pyruvate when the supply of C4 compounds is abundant.

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `activates` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00227|molecule.C00227]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.MALIC-NADP-CPLX|complex.ecocyc.MALIC-NADP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00575|molecule.C00575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MALIC-NADP-RXN`

## Notes

NADP + MAL -> NADPH + CARBON-DIOXIDE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
