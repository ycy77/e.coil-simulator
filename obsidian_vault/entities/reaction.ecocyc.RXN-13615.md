---
entity_id: "reaction.ecocyc.RXN-13615"
entity_type: "reaction"
name: "RXN-13615"
source_database: "EcoCyc"
source_id: "RXN-13615"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13615

`reaction.ecocyc.RXN-13615`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13615`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10267 + ETF-Oxidized + PROTON -> T2-DECENOYL-COA + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: CPD-10267 + ETF-Oxidized + PROTON -> T2-DECENOYL-COA + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Decanoyl-CoA (molecule.C05274). Products: trans-Dec-2-enoyl-CoA (molecule.C05275).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-10267 + ETF-Oxidized + PROTON -> T2-DECENOYL-COA + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C05275|molecule.C05275]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05274|molecule.C05274]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13615`

## Notes

CPD-10267 + ETF-Oxidized + PROTON -> T2-DECENOYL-COA + ETF-Reduced; direction=REVERSIBLE
