---
entity_id: "reaction.ecocyc.RXN0-1602"
entity_type: "reaction"
name: "RXN0-1602"
source_database: "EcoCyc"
source_id: "RXN0-1602"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1602

`reaction.ecocyc.RXN0-1602`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1602`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DITP + WATER -> PROTON + DIMP + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DITP + WATER -> PROTON + DIMP + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dITP/XTP pyrophosphatase (complex.ecocyc.CPLX0-7826). Substrates: H2O (molecule.C00001), dITP (molecule.C01345). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), 2'-Deoxyinosine 5'-phosphate (molecule.C06196).

## Annotation

DITP + WATER -> PROTON + DIMP + PPI; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7826|complex.ecocyc.CPLX0-7826]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06196|molecule.C06196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01345|molecule.C01345]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1602`

## Notes

DITP + WATER -> PROTON + DIMP + PPI; direction=LEFT-TO-RIGHT
