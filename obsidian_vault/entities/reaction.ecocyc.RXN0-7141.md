---
entity_id: "reaction.ecocyc.RXN0-7141"
entity_type: "reaction"
name: "RXN0-7141"
source_database: "EcoCyc"
source_id: "RXN0-7141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7141

`reaction.ecocyc.RXN0-7141`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7141`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is intentionally left unbalanced. report that the addition of 1 mM NADH, NADPH, or ATP to the reaction mixture (at 1 mM) did not yield an increase in DXP levels. EcoCyc reaction equation: DEOXYXYLULOSE-5P -> RIBULOSE-5P; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is intentionally left unbalanced. report that the addition of 1 mM NADH, NADPH, or ATP to the reaction mixture (at 1 mM) did not yield an increase in DXP levels.

## Biological Role

Catalyzed by yajO (protein.P77735). Substrates: 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437). Products: D-Ribulose 5-phosphate (molecule.C00199).

## Annotation

This reaction is intentionally left unbalanced. report that the addition of 1 mM NADH, NADPH, or ATP to the reaction mixture (at 1 mM) did not yield an increase in DXP levels.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77735|protein.P77735]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7141`

## Notes

DEOXYXYLULOSE-5P -> RIBULOSE-5P; direction=PHYSIOL-RIGHT-TO-LEFT
