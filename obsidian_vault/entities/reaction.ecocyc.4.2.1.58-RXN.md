---
entity_id: "reaction.ecocyc.4.2.1.58-RXN"
entity_type: "reaction"
name: "(3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydratase"
source_database: "EcoCyc"
source_id: "4.2.1.58-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# (3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydratase

`reaction.ecocyc.4.2.1.58-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4.2.1.58-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Beta-3-hydroxybutyryl-ACPs -> WATER + Crotonyl-ACPs; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Beta-3-hydroxybutyryl-ACPs -> WATER + Crotonyl-ACPs; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX). Products: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Beta-3-hydroxybutyryl-ACPs -> WATER + Crotonyl-ACPs; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:4.2.1.58-RXN`

## Notes

Beta-3-hydroxybutyryl-ACPs -> WATER + Crotonyl-ACPs; direction=PHYSIOL-LEFT-TO-RIGHT
