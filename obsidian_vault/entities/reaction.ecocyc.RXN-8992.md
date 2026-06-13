---
entity_id: "reaction.ecocyc.RXN-8992"
entity_type: "reaction"
name: "RXN-8992"
source_database: "EcoCyc"
source_id: "RXN-8992"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Prenyltransferase"
  - "Geranyl-diphosphate synthase"
---

# RXN-8992

`reaction.ecocyc.RXN-8992`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8992`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> OCTAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> OCTAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by all-trans-octaprenyl-diphosphate synthase (complex.ecocyc.CPLX0-7426). Substrates: Isopentenyl diphosphate (molecule.C00129), trans,trans-Farnesyl diphosphate (molecule.C00448). Products: Diphosphate (molecule.C00013), all-trans-Octaprenyl diphosphate (molecule.C04146).

## Enriched Pathways

- `ecocyc.PWY-5783` all-trans-octaprenyl diphosphate biosynthesis (EcoCyc)

## Annotation

FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> OCTAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5783` all-trans-octaprenyl diphosphate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7426|complex.ecocyc.CPLX0-7426]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04146|molecule.C04146]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00129|molecule.C00129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00448|molecule.C00448]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8992`

## Notes

FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> OCTAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT
