---
entity_id: "reaction.ecocyc.RXN0-307"
entity_type: "reaction"
name: "RXN0-307"
source_database: "EcoCyc"
source_id: "RXN0-307"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-307

`reaction.ecocyc.RXN0-307`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-307`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Red-Hybrid-Cluster-Proteins + NAD -> Ox-Hybrid-Cluster-Proteins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Red-Hybrid-Cluster-Proteins + NAD -> Ox-Hybrid-Cluster-Proteins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by hcr (protein.P75824). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004).

## Annotation

Red-Hybrid-Cluster-Proteins + NAD -> Ox-Hybrid-Cluster-Proteins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P75824|protein.P75824]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-307`

## Notes

Red-Hybrid-Cluster-Proteins + NAD -> Ox-Hybrid-Cluster-Proteins + NADH; direction=PHYSIOL-RIGHT-TO-LEFT
