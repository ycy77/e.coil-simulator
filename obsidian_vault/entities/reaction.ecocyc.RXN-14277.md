---
entity_id: "reaction.ecocyc.RXN-14277"
entity_type: "reaction"
name: "hexanoyl-CoA C-acyltransferase"
source_database: "EcoCyc"
source_id: "RXN-14277"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hexanoyl-CoA C-acyltransferase

`reaction.ecocyc.RXN-14277`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14277`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HEXANOYL-COA + ACETYL-COA -> CPD0-2106 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: HEXANOYL-COA + ACETYL-COA -> CPD0-2106 + CO-A; direction=REVERSIBLE.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), Hexanoyl-CoA (molecule.C05270). Products: CoA (molecule.C00010), 3-Oxooctanoyl-CoA (molecule.C05267).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

HEXANOYL-COA + ACETYL-COA -> CPD0-2106 + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05267|molecule.C05267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05270|molecule.C05270]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14277`

## Notes

HEXANOYL-COA + ACETYL-COA -> CPD0-2106 + CO-A; direction=REVERSIBLE
