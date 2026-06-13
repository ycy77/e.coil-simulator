---
entity_id: "reaction.ecocyc.ALDOSE1EPIM-RXN"
entity_type: "reaction"
name: "ALDOSE1EPIM-RXN"
source_database: "EcoCyc"
source_id: "ALDOSE1EPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALDOSE1EPIM-RXN

`reaction.ecocyc.ALDOSE1EPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALDOSE1EPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in galactose metabolism. It funnels β-galactose into reactions of α-galactose catabolism. EcoCyc reaction equation: GALACTOSE -> ALPHA-D-GALACTOSE; direction=REVERSIBLE. This reaction is involved in galactose metabolism. It funnels β-galactose into reactions of α-galactose catabolism.

## Biological Role

Catalyzed by galM (protein.P0A9C3). Substrates: β-D-galactopyranose (molecule.ecocyc.GALACTOSE). Products: alpha-D-Galactose (molecule.C00984).

## Enriched Pathways

- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)

## Annotation

This reaction is involved in galactose metabolism. It funnels β-galactose into reactions of α-galactose catabolism.

## Pathways

- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9C3|protein.P0A9C3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00984|molecule.C00984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.GALACTOSE__677c1dad|molecule.ecocyc.GALACTOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00159|molecule.C00159]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-DEOXY-D-GLUCOSE|molecule.ecocyc.2-DEOXY-D-GLUCOSE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALDOSE1EPIM-RXN`

## Notes

GALACTOSE -> ALPHA-D-GALACTOSE; direction=REVERSIBLE
