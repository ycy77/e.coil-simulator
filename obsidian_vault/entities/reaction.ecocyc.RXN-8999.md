---
entity_id: "reaction.ecocyc.RXN-8999"
entity_type: "reaction"
name: "RXN-8999"
source_database: "EcoCyc"
source_id: "RXN-8999"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8999

`reaction.ecocyc.RXN-8999`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8999`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> UNDECAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> UNDECAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ditrans,polycis-undecaprenyl-diphosphate synthase [(2E,6E)-farnesyl-diphosphate specific] (complex.ecocyc.UPPSYN-CPLX). Substrates: Isopentenyl diphosphate (molecule.C00129), trans,trans-Farnesyl diphosphate (molecule.C00448). Products: Diphosphate (molecule.C00013), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574).

## Enriched Pathways

- `ecocyc.PWY-5785` di-trans,poly-cis-undecaprenyl phosphate biosynthesis (EcoCyc)

## Annotation

FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> UNDECAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5785` di-trans,poly-cis-undecaprenyl phosphate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.UPPSYN-CPLX|complex.ecocyc.UPPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00129|molecule.C00129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00448|molecule.C00448]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8999`

## Notes

FARNESYL-PP + DELTA3-ISOPENTENYL-PP -> UNDECAPRENYL-DIPHOSPHATE + PPI; direction=LEFT-TO-RIGHT
