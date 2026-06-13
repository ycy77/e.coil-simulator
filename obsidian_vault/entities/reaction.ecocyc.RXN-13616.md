---
entity_id: "reaction.ecocyc.RXN-13616"
entity_type: "reaction"
name: "RXN-13616"
source_database: "EcoCyc"
source_id: "RXN-13616"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13616

`reaction.ecocyc.RXN-13616`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13616`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2244 -> T2-DECENOYL-COA + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2244 -> T2-DECENOYL-COA + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: (S)-Hydroxydecanoyl-CoA (molecule.C05264). Products: H2O (molecule.C00001), trans-Dec-2-enoyl-CoA (molecule.C05275).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-2244 -> T2-DECENOYL-COA + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05275|molecule.C05275]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05264|molecule.C05264]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13616`

## Notes

CPD0-2244 -> T2-DECENOYL-COA + WATER; direction=REVERSIBLE
