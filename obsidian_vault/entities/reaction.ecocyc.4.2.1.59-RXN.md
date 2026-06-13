---
entity_id: "reaction.ecocyc.4.2.1.59-RXN"
entity_type: "reaction"
name: "4.2.1.59-RXN"
source_database: "EcoCyc"
source_id: "4.2.1.59-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4.2.1.59-RXN

`reaction.ecocyc.4.2.1.59-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4.2.1.59-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Hydroxy-octanoyl-ACPs -> 2-Octenoyl-ACPs + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 3-Hydroxy-octanoyl-ACPs -> 2-Octenoyl-ACPs + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-hydroxy-acyl-[acyl-carrier-protein] dehydratase (complex.ecocyc.FABZ-CPLX). Products: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

3-Hydroxy-octanoyl-ACPs -> 2-Octenoyl-ACPs + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.FABZ-CPLX|complex.ecocyc.FABZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:4.2.1.59-RXN`

## Notes

3-Hydroxy-octanoyl-ACPs -> 2-Octenoyl-ACPs + WATER; direction=LEFT-TO-RIGHT
