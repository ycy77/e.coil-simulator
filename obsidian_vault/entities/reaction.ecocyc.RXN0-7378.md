---
entity_id: "reaction.ecocyc.RXN0-7378"
entity_type: "reaction"
name: "RXN0-7378"
source_database: "EcoCyc"
source_id: "RXN0-7378"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7378

`reaction.ecocyc.RXN0-7378`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7378`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PIIPROTEIN-CPLX + UTP -> CPLX0-8568 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PIIPROTEIN-CPLX + UTP -> CPLX0-8568 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glnD (protein.P27249). Substrates: UTP (molecule.C00075). Products: Diphosphate (molecule.C00013).

## Annotation

PIIPROTEIN-CPLX + UTP -> CPLX0-8568 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P27249|protein.P27249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7378`

## Notes

PIIPROTEIN-CPLX + UTP -> CPLX0-8568 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
