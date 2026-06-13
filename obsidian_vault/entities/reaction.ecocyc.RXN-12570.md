---
entity_id: "reaction.ecocyc.RXN-12570"
entity_type: "reaction"
name: "RXN-12570"
source_database: "EcoCyc"
source_id: "RXN-12570"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12570

`reaction.ecocyc.RXN-12570`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12570`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OH-HEXANOYL-COA + NAD -> K-HEXANOYL-COA + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: OH-HEXANOYL-COA + NAD -> K-HEXANOYL-COA + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), (S)-Hydroxyhexanoyl-CoA (molecule.C05268). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Oxohexanoyl-CoA (molecule.C05269).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

OH-HEXANOYL-COA + NAD -> K-HEXANOYL-COA + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05269|molecule.C05269]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05268|molecule.C05268]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12570`

## Notes

OH-HEXANOYL-COA + NAD -> K-HEXANOYL-COA + NADH + PROTON; direction=LEFT-TO-RIGHT
