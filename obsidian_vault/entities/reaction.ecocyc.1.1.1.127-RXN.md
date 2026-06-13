---
entity_id: "reaction.ecocyc.1.1.1.127-RXN"
entity_type: "reaction"
name: "1.1.1.127-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.127-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.127-RXN

`reaction.ecocyc.1.1.1.127-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.127-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-DEHYDRO-3-DEOXY-D-GLUCONATE + NAD -> CPD-343 + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: 2-DEHYDRO-3-DEOXY-D-GLUCONATE + NAD -> CPD-343 + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by kduD (protein.P37769). Substrates: NAD+ (molecule.C00003), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204). Products: NADH (molecule.C00004), H+ (molecule.C00080), (4S)-4,6-Dihydroxy-2,5-dioxohexanoate (molecule.C04349).

## Enriched Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

2-DEHYDRO-3-DEOXY-D-GLUCONATE + NAD -> CPD-343 + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37769|protein.P37769]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04349|molecule.C04349]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.127-RXN`

## Notes

2-DEHYDRO-3-DEOXY-D-GLUCONATE + NAD -> CPD-343 + NADH + PROTON; direction=REVERSIBLE
