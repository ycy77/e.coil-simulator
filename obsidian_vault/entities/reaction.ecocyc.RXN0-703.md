---
entity_id: "reaction.ecocyc.RXN0-703"
entity_type: "reaction"
name: "RXN0-703"
source_database: "EcoCyc"
source_id: "RXN0-703"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-703

`reaction.ecocyc.RXN0-703`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-703`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-KETO-L-GULONATE + NAD -> PROTON + CPD-334 + NADH; direction=RIGHT-TO-LEFT EcoCyc reaction equation: 3-KETO-L-GULONATE + NAD -> PROTON + CPD-334 + NADH; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 2,3-diketo-L-gulonate reductase (complex.ecocyc.CPLX0-2061). Substrates: NAD+ (molecule.C00003), 3-Dehydro-L-gulonate (molecule.C00618). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2,3-didehydro-L-gulonate (molecule.ecocyc.CPD-334).

## Enriched Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Annotation

3-KETO-L-GULONATE + NAD -> PROTON + CPD-334 + NADH; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2061|complex.ecocyc.CPLX0-2061]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-334|molecule.ecocyc.CPD-334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00618|molecule.C00618]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-703`

## Notes

3-KETO-L-GULONATE + NAD -> PROTON + CPD-334 + NADH; direction=RIGHT-TO-LEFT
