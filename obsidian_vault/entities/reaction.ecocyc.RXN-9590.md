---
entity_id: "reaction.ecocyc.RXN-9590"
entity_type: "reaction"
name: "RXN-9590"
source_database: "EcoCyc"
source_id: "RXN-9590"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9590

`reaction.ecocyc.RXN-9590`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9590`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Fatty-acyl-ACPs + Pi -> Acyl-Phosphates + ACP; direction=REVERSIBLE EcoCyc reaction equation: Fatty-acyl-ACPs + Pi -> Acyl-Phosphates + ACP; direction=REVERSIBLE.

## Biological Role

Catalyzed by plsX (protein.P27247). Substrates: phosphate (molecule.ecocyc.Pi). Products: Acyl phosphate (molecule.C02133).

## Annotation

Fatty-acyl-ACPs + Pi -> Acyl-Phosphates + ACP; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27247|protein.P27247]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C02133|molecule.C02133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9590`

## Notes

Fatty-acyl-ACPs + Pi -> Acyl-Phosphates + ACP; direction=REVERSIBLE
