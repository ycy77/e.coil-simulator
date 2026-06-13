---
entity_id: "reaction.ecocyc.RXN-12567"
entity_type: "reaction"
name: "RXN-12567"
source_database: "EcoCyc"
source_id: "RXN-12567"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12567

`reaction.ecocyc.RXN-12567`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12567`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OH-HEXANOYL-COA -> CPD0-2121 + WATER; direction=REVERSIBLE EcoCyc reaction equation: OH-HEXANOYL-COA -> CPD0-2121 + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: (S)-Hydroxyhexanoyl-CoA (molecule.C05268). Products: H2O (molecule.C00001), trans-Hex-2-enoyl-CoA (molecule.C05271).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

OH-HEXANOYL-COA -> CPD0-2121 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05271|molecule.C05271]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05268|molecule.C05268]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12567`

## Notes

OH-HEXANOYL-COA -> CPD0-2121 + WATER; direction=REVERSIBLE
