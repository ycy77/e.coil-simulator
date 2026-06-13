---
entity_id: "reaction.ecocyc.RXN-9549"
entity_type: "reaction"
name: "RXN-9549"
source_database: "EcoCyc"
source_id: "RXN-9549"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9549

`reaction.ecocyc.RXN-9549`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9549`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Palmitoyl-ACPs + WATER -> PALMITATE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Palmitoyl-ACPs + WATER -> PALMITATE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), Hexadecanoic acid (molecule.C00249).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Palmitoyl-ACPs + WATER -> PALMITATE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00249|molecule.C00249]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9549`

## Notes

Palmitoyl-ACPs + WATER -> PALMITATE + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
