---
entity_id: "reaction.ecocyc.RXN0-4342"
entity_type: "reaction"
name: "RXN0-4342"
source_database: "EcoCyc"
source_id: "RXN0-4342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4342

`reaction.ecocyc.RXN0-4342`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4342`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + D-BETA-D-HEPTOSE-1-P + ATP -> ADP-D-GLYCERO-D-MANNO-HEPTOSE + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + D-BETA-D-HEPTOSE-1-P + ATP -> ADP-D-GLYCERO-D-MANNO-HEPTOSE + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fused heptose 7-phosphate kinase/heptose 1-phosphate adenyltransferase (complex.ecocyc.CPLX0-3661). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), D-glycero-beta-D-manno-Heptose 1-phosphate (molecule.C07838). Products: Diphosphate (molecule.C00013), ADP-D-glycero-beta-D-manno-heptose (molecule.C06397).

## Enriched Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Annotation

PROTON + D-BETA-D-HEPTOSE-1-P + ATP -> ADP-D-GLYCERO-D-MANNO-HEPTOSE + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3661|complex.ecocyc.CPLX0-3661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06397|molecule.C06397]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C07838|molecule.C07838]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4342`

## Notes

PROTON + D-BETA-D-HEPTOSE-1-P + ATP -> ADP-D-GLYCERO-D-MANNO-HEPTOSE + PPI; direction=LEFT-TO-RIGHT
