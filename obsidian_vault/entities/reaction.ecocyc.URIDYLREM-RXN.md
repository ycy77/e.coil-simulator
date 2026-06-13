---
entity_id: "reaction.ecocyc.URIDYLREM-RXN"
entity_type: "reaction"
name: "URIDYLREM-RXN"
source_database: "EcoCyc"
source_id: "URIDYLREM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URIDYLREM-RXN

`reaction.ecocyc.URIDYLREM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URIDYLREM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the glutamine synthetase cascade. EcoCyc reaction equation: CPLX0-8568 + WATER -> PIIPROTEIN-CPLX + UMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the glutamine synthetase cascade.

## Biological Role

Catalyzed by glnD (protein.P27249). Substrates: H2O (molecule.C00001). Products: UMP (molecule.C00105).

## Annotation

This reaction is part of the glutamine synthetase cascade.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P27249|protein.P27249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:URIDYLREM-RXN`

## Notes

CPLX0-8568 + WATER -> PIIPROTEIN-CPLX + UMP; direction=PHYSIOL-LEFT-TO-RIGHT
