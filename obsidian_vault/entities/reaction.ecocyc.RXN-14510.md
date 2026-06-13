---
entity_id: "reaction.ecocyc.RXN-14510"
entity_type: "reaction"
name: "RXN-14510"
source_database: "EcoCyc"
source_id: "RXN-14510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14510

`reaction.ecocyc.RXN-14510`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14510`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3723 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3723 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), uridine 2'-monophosphate (molecule.ecocyc.CPD-3723). Products: Uridine (molecule.C00299), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3723 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3723|molecule.ecocyc.CPD-3723]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14510`

## Notes

CPD-3723 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
