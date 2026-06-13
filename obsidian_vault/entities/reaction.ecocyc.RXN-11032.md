---
entity_id: "reaction.ecocyc.RXN-11032"
entity_type: "reaction"
name: "RXN-11032"
source_database: "EcoCyc"
source_id: "RXN-11032"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11032

`reaction.ecocyc.RXN-11032`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11032`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-255 + NAD -> DIACETYL + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: CPD-255 + NAD -> DIACETYL + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ucpA (protein.P37440). Substrates: NAD+ (molecule.C00003), (S)-Acetoin (molecule.C01769). Products: NADH (molecule.C00004), H+ (molecule.C00080), Diacetyl (molecule.C00741).

## Annotation

CPD-255 + NAD -> DIACETYL + NADH + PROTON; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37440|protein.P37440]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00741|molecule.C00741]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01769|molecule.C01769]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11032`

## Notes

CPD-255 + NAD -> DIACETYL + NADH + PROTON; direction=RIGHT-TO-LEFT
