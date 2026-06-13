---
entity_id: "reaction.ecocyc.RHAMNISOM-RXN"
entity_type: "reaction"
name: "RHAMNISOM-RXN"
source_database: "EcoCyc"
source_id: "RHAMNISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RHAMNISOM-RXN

`reaction.ecocyc.RHAMNISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RHAMNISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step in L-rhamnose catabolism. EcoCyc reaction equation: CPD0-1112 -> CPD-16566; direction=REVERSIBLE. The first step in L-rhamnose catabolism.

## Biological Role

Catalyzed by L-rhamnose isomerase (complex.ecocyc.CPLX0-7652). Substrates: β-L-rhamnopyranose (molecule.ecocyc.CPD0-1112). Products: L-Rhamnulose (molecule.C00861).

## Enriched Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Annotation

The first step in L-rhamnose catabolism.

## Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7652|complex.ecocyc.CPLX0-7652]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00861|molecule.C00861]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1112|molecule.ecocyc.CPD0-1112]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1114|molecule.ecocyc.CPD0-1114]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RHAMNISOM-RXN`

## Notes

CPD0-1112 -> CPD-16566; direction=REVERSIBLE
