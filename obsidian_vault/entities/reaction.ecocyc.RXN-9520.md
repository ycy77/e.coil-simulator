---
entity_id: "reaction.ecocyc.RXN-9520"
entity_type: "reaction"
name: "RXN-9520"
source_database: "EcoCyc"
source_id: "RXN-9520"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9520

`reaction.ecocyc.RXN-9520`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9520`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

R-3-hydroxyhexanoyl-ACPs -> Hex-2-enoyl-ACPs + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: R-3-hydroxyhexanoyl-ACPs -> Hex-2-enoyl-ACPs + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX). Products: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

R-3-hydroxyhexanoyl-ACPs -> Hex-2-enoyl-ACPs + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-9520`

## Notes

R-3-hydroxyhexanoyl-ACPs -> Hex-2-enoyl-ACPs + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
