---
entity_id: "reaction.ecocyc.RXN-16804"
entity_type: "reaction"
name: "RXN-16804"
source_database: "EcoCyc"
source_id: "RXN-16804"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16804

`reaction.ecocyc.RXN-16804`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16804`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ARABINOSE-5P -> CPD-18118; direction=REVERSIBLE EcoCyc reaction equation: ARABINOSE-5P -> CPD-18118; direction=REVERSIBLE.

## Biological Role

Substrates: D-Arabinose 5-phosphate (molecule.C01112). Products: D-arabinofuranose 5-phosphate (molecule.ecocyc.CPD-18118).

## Enriched Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Annotation

ARABINOSE-5P -> CPD-18118; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-18118|molecule.ecocyc.CPD-18118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01112|molecule.C01112]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16804`

## Notes

ARABINOSE-5P -> CPD-18118; direction=REVERSIBLE
