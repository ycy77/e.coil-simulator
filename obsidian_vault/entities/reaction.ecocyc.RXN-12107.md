---
entity_id: "reaction.ecocyc.RXN-12107"
entity_type: "reaction"
name: "L-idonate:NAD(P)+ oxidoreductase"
source_database: "EcoCyc"
source_id: "RXN-12107"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-idonate:NAD(P)+ oxidoreductase

`reaction.ecocyc.RXN-12107`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12107`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-IDONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-IDONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), L-idonate (molecule.ecocyc.L-IDONATE). Products: NADH (molecule.C00004), H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE).

## Annotation

L-IDONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12107`

## Notes

L-IDONATE + NAD -> 5-DEHYDROGLUCONATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
