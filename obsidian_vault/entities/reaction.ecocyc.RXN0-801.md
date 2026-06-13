---
entity_id: "reaction.ecocyc.RXN0-801"
entity_type: "reaction"
name: "RXN0-801"
source_database: "EcoCyc"
source_id: "RXN0-801"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-801

`reaction.ecocyc.RXN0-801`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-801`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PII2-CPLX + UTP -> PPI + CPLX0-8570; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PII2-CPLX + UTP -> PPI + CPLX0-8570; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glnD (protein.P27249). Substrates: UTP (molecule.C00075). Products: Diphosphate (molecule.C00013).

## Annotation

PII2-CPLX + UTP -> PPI + CPLX0-8570; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27249|protein.P27249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-801`

## Notes

PII2-CPLX + UTP -> PPI + CPLX0-8570; direction=PHYSIOL-LEFT-TO-RIGHT
