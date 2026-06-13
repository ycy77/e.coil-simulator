---
entity_id: "reaction.ecocyc.RXN66-448"
entity_type: "reaction"
name: "RXN66-448"
source_database: "EcoCyc"
source_id: "RXN66-448"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN66-448

`reaction.ecocyc.RXN66-448`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN66-448`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ARG -> ARG; direction=RIGHT-TO-LEFT EcoCyc reaction equation: ARG -> ARG; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by argO (protein.P11667). Substrates: L-Arginine (molecule.C00062). Products: L-Arginine (molecule.C00062).

## Annotation

ARG -> ARG; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P11667|protein.P11667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN66-448`

## Notes

ARG -> ARG; direction=RIGHT-TO-LEFT
