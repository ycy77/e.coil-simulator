---
entity_id: "reaction.ecocyc.RXN-20678"
entity_type: "reaction"
name: "RXN-20678"
source_database: "EcoCyc"
source_id: "RXN-20678"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20678

`reaction.ecocyc.RXN-20678`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20678`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22313 -> CPD0-2108 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-22313 -> CPD0-2108 + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: (3S)-3-hydroxyoctanoyl-CoA (molecule.ecocyc.CPD-22313). Products: H2O (molecule.C00001), trans-Oct-2-enoyl-CoA (molecule.C05276).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-22313 -> CPD0-2108 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05276|molecule.C05276]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22313|molecule.ecocyc.CPD-22313]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20678`

## Notes

CPD-22313 -> CPD0-2108 + WATER; direction=REVERSIBLE
