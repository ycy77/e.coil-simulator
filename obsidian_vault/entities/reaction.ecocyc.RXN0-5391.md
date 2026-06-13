---
entity_id: "reaction.ecocyc.RXN0-5391"
entity_type: "reaction"
name: "RXN0-5391"
source_database: "EcoCyc"
source_id: "RXN0-5391"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5391

`reaction.ecocyc.RXN0-5391`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5391`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1162 -> CPD0-1158; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1162 -> CPD0-1158; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177). Substrates: (2E,5Z)-tetradec-2,5-enoyl-CoA (molecule.ecocyc.CPD0-1162). Products: (3E,5Z)-tetradeca-3,5-dienoyl-CoA (molecule.ecocyc.CPD0-1158).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-1162 -> CPD0-1158; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1158|molecule.ecocyc.CPD0-1158]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1162|molecule.ecocyc.CPD0-1162]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5391`

## Notes

CPD0-1162 -> CPD0-1158; direction=REVERSIBLE
