---
entity_id: "reaction.ecocyc.RXN-20675"
entity_type: "reaction"
name: "RXN-20675"
source_database: "EcoCyc"
source_id: "RXN-20675"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20675

`reaction.ecocyc.RXN-20675`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20675`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2107 -> CPD-7222 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2107 -> CPD-7222 + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: (S)-3-Hydroxydodecanoyl-CoA (molecule.C05262). Products: H2O (molecule.C00001), 2-trans-Dodecenoyl-CoA (molecule.C03221).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-2107 -> CPD-7222 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03221|molecule.C03221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05262|molecule.C05262]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20675`

## Notes

CPD0-2107 -> CPD-7222 + WATER; direction=REVERSIBLE
