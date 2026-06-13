---
entity_id: "reaction.ecocyc.RXN-9510"
entity_type: "reaction"
name: "RXN-9510"
source_database: "EcoCyc"
source_id: "RXN-9510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9510

`reaction.ecocyc.RXN-9510`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9510`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FMNH2 + NAD -> FMN + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: FMNH2 + NAD -> FMN + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by rutF (protein.P75893). Substrates: NAD+ (molecule.C00003), Reduced FMN (molecule.C01847). Products: NADH (molecule.C00004), FMN (molecule.C00061), H+ (molecule.C00080).

## Annotation

FMNH2 + NAD -> FMN + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75893|protein.P75893]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9510`

## Notes

FMNH2 + NAD -> FMN + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
