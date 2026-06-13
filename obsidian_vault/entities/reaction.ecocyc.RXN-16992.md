---
entity_id: "reaction.ecocyc.RXN-16992"
entity_type: "reaction"
name: "RXN-16992"
source_database: "EcoCyc"
source_id: "RXN-16992"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16992

`reaction.ecocyc.RXN-16992`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16992`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TAGATOSE-6-PHOSPHATE -> CPD-15826; direction=REVERSIBLE EcoCyc reaction equation: TAGATOSE-6-PHOSPHATE -> CPD-15826; direction=REVERSIBLE.

## Biological Role

Substrates: D-Tagatose 6-phosphate (molecule.C01097). Products: keto-D-tagatose 6-phosphate (molecule.ecocyc.CPD-15826).

## Enriched Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Annotation

TAGATOSE-6-PHOSPHATE -> CPD-15826; direction=REVERSIBLE

## Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-15826|molecule.ecocyc.CPD-15826]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01097|molecule.C01097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16992`

## Notes

TAGATOSE-6-PHOSPHATE -> CPD-15826; direction=REVERSIBLE
