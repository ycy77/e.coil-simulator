---
entity_id: "reaction.ecocyc.O-SUCCINYLBENZOATE-COA-SYN-RXN"
entity_type: "reaction"
name: "O-SUCCINYLBENZOATE-COA-SYN-RXN"
source_database: "EcoCyc"
source_id: "O-SUCCINYLBENZOATE-COA-SYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# O-SUCCINYLBENZOATE-COA-SYN-RXN

`reaction.ecocyc.O-SUCCINYLBENZOATE-COA-SYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:O-SUCCINYLBENZOATE-COA-SYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in menaquinone biosynthesis. EcoCyc reaction equation: CPD-9923 -> O-SUCCINYLBENZOATE + WATER; direction=LEFT-TO-RIGHT. This is the third reaction in menaquinone biosynthesis.

## Biological Role

Catalyzed by menC (protein.P29208). Substrates: (1R,6R)-6-Hydroxy-2-succinylcyclohexa-2,4-diene-1-carboxylate (molecule.C05817). Products: H2O (molecule.C00001), 2-Succinylbenzoate (molecule.C02730).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Annotation

This is the third reaction in menaquinone biosynthesis.

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P29208|protein.P29208]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02730|molecule.C02730]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05817|molecule.C05817]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:O-SUCCINYLBENZOATE-COA-SYN-RXN`

## Notes

CPD-9923 -> O-SUCCINYLBENZOATE + WATER; direction=LEFT-TO-RIGHT
