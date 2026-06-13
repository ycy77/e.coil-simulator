---
entity_id: "reaction.ecocyc.RXN0-4301"
entity_type: "reaction"
name: "RXN0-4301"
source_database: "EcoCyc"
source_id: "RXN0-4301"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4301

`reaction.ecocyc.RXN0-4301`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4301`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-SEDOHEPTULOSE-7-P -> D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-SEDOHEPTULOSE-7-P -> D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-sedoheptulose 7-phosphate isomerase (complex.ecocyc.CPLX0-7660). Substrates: Sedoheptulose 7-phosphate (molecule.C05382). Products: D-glycero-beta-D-manno-Heptose 7-phosphate (molecule.C07836).

## Enriched Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Annotation

D-SEDOHEPTULOSE-7-P -> D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7660|complex.ecocyc.CPLX0-7660]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C07836|molecule.C07836]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4301`

## Notes

D-SEDOHEPTULOSE-7-P -> D-ALPHABETA-D-HEPTOSE-7-PHOSPHATE; direction=LEFT-TO-RIGHT
