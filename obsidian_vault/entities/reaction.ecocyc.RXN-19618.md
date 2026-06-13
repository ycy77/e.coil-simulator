---
entity_id: "reaction.ecocyc.RXN-19618"
entity_type: "reaction"
name: "RXN-19618"
source_database: "EcoCyc"
source_id: "RXN-19618"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19618

`reaction.ecocyc.RXN-19618`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19618`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

TRIMETHYLAMINE + an-oxidized-TorC-protein + WATER -> TRIMETHYLAMINE-N-O + a-reduced-TorC-protein + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: TRIMETHYLAMINE + an-oxidized-TorC-protein + WATER -> TRIMETHYLAMINE-N-O + a-reduced-TorC-protein + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by torA (protein.P33225). Substrates: H2O (molecule.C00001), Trimethylamine (molecule.C00565). Products: H+ (molecule.C00080), Trimethylamine N-oxide (molecule.C01104).

## Annotation

TRIMETHYLAMINE + an-oxidized-TorC-protein + WATER -> TRIMETHYLAMINE-N-O + a-reduced-TorC-protein + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33225|protein.P33225]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01104|molecule.C01104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19618`

## Notes

TRIMETHYLAMINE + an-oxidized-TorC-protein + WATER -> TRIMETHYLAMINE-N-O + a-reduced-TorC-protein + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
