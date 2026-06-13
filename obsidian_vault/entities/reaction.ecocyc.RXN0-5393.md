---
entity_id: "reaction.ecocyc.RXN0-5393"
entity_type: "reaction"
name: "RXN0-5393"
source_database: "EcoCyc"
source_id: "RXN0-5393"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5393

`reaction.ecocyc.RXN0-5393`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5393`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1163 -> CPD0-1162 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1163 -> CPD0-1162 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: (S)-3-hydroxy-(5Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD0-1163). Products: H2O (molecule.C00001), (2E,5Z)-tetradec-2,5-enoyl-CoA (molecule.ecocyc.CPD0-1162).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-1163 -> CPD0-1162 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1162|molecule.ecocyc.CPD0-1162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1163|molecule.ecocyc.CPD0-1163]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5393`

## Notes

CPD0-1163 -> CPD0-1162 + WATER; direction=REVERSIBLE
