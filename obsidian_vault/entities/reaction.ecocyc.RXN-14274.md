---
entity_id: "reaction.ecocyc.RXN-14274"
entity_type: "reaction"
name: "decanoyl-CoA C-acyltransferase"
source_database: "EcoCyc"
source_id: "RXN-14274"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# decanoyl-CoA C-acyltransferase

`reaction.ecocyc.RXN-14274`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14274`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10267 + ACETYL-COA -> CPD0-2105 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: CPD-10267 + ACETYL-COA -> CPD0-2105 + CO-A; direction=REVERSIBLE.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), Decanoyl-CoA (molecule.C05274). Products: CoA (molecule.C00010), 3-Oxododecanoyl-CoA (molecule.C05263).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-10267 + ACETYL-COA -> CPD0-2105 + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05263|molecule.C05263]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05274|molecule.C05274]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14274`

## Notes

CPD-10267 + ACETYL-COA -> CPD0-2105 + CO-A; direction=REVERSIBLE
