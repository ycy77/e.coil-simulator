---
entity_id: "reaction.ecocyc.RXN-16964"
entity_type: "reaction"
name: "RXN-16964"
source_database: "EcoCyc"
source_id: "RXN-16964"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16964

`reaction.ecocyc.RXN-16964`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16964`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12349 + NAD -> CPD-343 + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12349 + NAD -> CPD-343 + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), 2-Dehydro-3-deoxy-L-galactonate (molecule.C20680). Products: NADH (molecule.C00004), H+ (molecule.C00080), (4S)-4,6-Dihydroxy-2,5-dioxohexanoate (molecule.C04349).

## Enriched Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

CPD-12349 + NAD -> CPD-343 + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04349|molecule.C04349]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20680|molecule.C20680]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16964`

## Notes

CPD-12349 + NAD -> CPD-343 + NADH + PROTON; direction=LEFT-TO-RIGHT
