---
entity_id: "reaction.ecocyc.RXN0-4341"
entity_type: "reaction"
name: "RXN0-4341"
source_database: "EcoCyc"
source_id: "RXN0-4341"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4341

`reaction.ecocyc.RXN0-4341`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4341`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE + ATP -> PROTON + D-BETA-D-HEPTOSE-17-DIPHOSPHATE + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE + ATP -> PROTON + D-BETA-D-HEPTOSE-17-DIPHOSPHATE + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fused heptose 7-phosphate kinase/heptose 1-phosphate adenyltransferase (complex.ecocyc.CPLX0-3661). Substrates: ATP (molecule.C00002), D-glycero-beta-D-manno-Heptose 7-phosphate (molecule.C07836). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-glycero-beta-D-manno-Heptose 1,7-bisphosphate (molecule.C11472).

## Enriched Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Annotation

D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE + ATP -> PROTON + D-BETA-D-HEPTOSE-17-DIPHOSPHATE + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3661|complex.ecocyc.CPLX0-3661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11472|molecule.C11472]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C07836|molecule.C07836]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4341`

## Notes

D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE + ATP -> PROTON + D-BETA-D-HEPTOSE-17-DIPHOSPHATE + ADP; direction=LEFT-TO-RIGHT
