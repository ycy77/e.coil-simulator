---
entity_id: "reaction.ecocyc.RXN-16819"
entity_type: "reaction"
name: "RXN-16819"
source_database: "EcoCyc"
source_id: "RXN-16819"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16819

`reaction.ecocyc.RXN-16819`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16819`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MAL + PROTON -> L-LACTATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MAL + PROTON -> L-LACTATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by malate dehydrogenase (oxaloacetate-decarboxylating) (NADP+) (complex.ecocyc.MALIC-NADP-CPLX). Substrates: H+ (molecule.C00080), (S)-Malate (molecule.C00149). Products: CO2 (molecule.C00011), (S)-Lactate (molecule.C00186).

## Annotation

MAL + PROTON -> L-LACTATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.MALIC-NADP-CPLX|complex.ecocyc.MALIC-NADP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16819`

## Notes

MAL + PROTON -> L-LACTATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
