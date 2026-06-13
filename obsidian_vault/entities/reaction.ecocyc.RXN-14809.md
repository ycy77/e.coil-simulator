---
entity_id: "reaction.ecocyc.RXN-14809"
entity_type: "reaction"
name: "RXN-14809"
source_database: "EcoCyc"
source_id: "RXN-14809"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14809

`reaction.ecocyc.RXN-14809`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14809`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-arabinofuranose -> L-arabinopyranose; direction=REVERSIBLE EcoCyc reaction equation: L-arabinofuranose -> L-arabinopyranose; direction=REVERSIBLE.

## Biological Role

Substrates: L-arabinofuranose (molecule.ecocyc.L-arabinofuranose). Products: L-Arabinose (molecule.C00259).

## Enriched Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)

## Annotation

L-arabinofuranose -> L-arabinopyranose; direction=REVERSIBLE

## Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-arabinofuranose|molecule.ecocyc.L-arabinofuranose]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14809`

## Notes

L-arabinofuranose -> L-arabinopyranose; direction=REVERSIBLE
