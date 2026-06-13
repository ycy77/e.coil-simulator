---
entity_id: "reaction.ecocyc.NRIIPHOS-RXN"
entity_type: "reaction"
name: "NRIIPHOS-RXN"
source_database: "EcoCyc"
source_id: "NRIIPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NRIIPHOS-RXN

`reaction.ecocyc.NRIIPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NRIIPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is reversible in vitro . EcoCyc reaction equation: GLNL-CPLX + ATP -> PROTEIN-NRIIP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is reversible in vitro .

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1509` NtrBC Two-Component Regulatory System (EcoCyc)

## Annotation

This reaction is reversible in vitro .

## Pathways

- `ecocyc.PWY0-1509` NtrBC Two-Component Regulatory System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[complex.ecocyc.PIIPROTEIN-CPLX|complex.ecocyc.PIIPROTEIN-CPLX]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions

## External IDs

- `EcoCyc:NRIIPHOS-RXN`

## Notes

GLNL-CPLX + ATP -> PROTEIN-NRIIP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
