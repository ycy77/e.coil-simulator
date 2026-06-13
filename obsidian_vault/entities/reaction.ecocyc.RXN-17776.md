---
entity_id: "reaction.ecocyc.RXN-17776"
entity_type: "reaction"
name: "RXN-17776"
source_database: "EcoCyc"
source_id: "RXN-17776"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17776

`reaction.ecocyc.RXN-17776`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17776`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19171 -> CPD-19172 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-19171 -> CPD-19172 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: (S)-3-hydroxy-(9Z)-octadecenoyl-CoA (molecule.ecocyc.CPD-19171). Products: H2O (molecule.C00001), (2E,9Z)-octadec-2,9-enoyl-CoA (molecule.ecocyc.CPD-19172).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-19171 -> CPD-19172 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19172|molecule.ecocyc.CPD-19172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19171|molecule.ecocyc.CPD-19171]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17776`

## Notes

CPD-19171 -> CPD-19172 + WATER; direction=REVERSIBLE
