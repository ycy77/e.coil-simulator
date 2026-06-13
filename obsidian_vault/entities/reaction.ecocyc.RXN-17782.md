---
entity_id: "reaction.ecocyc.RXN-17782"
entity_type: "reaction"
name: "RXN-17782"
source_database: "EcoCyc"
source_id: "RXN-17782"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17782

`reaction.ecocyc.RXN-17782`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17782`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15436 + ACETYL-COA -> CPD-19167 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: CPD-15436 + ACETYL-COA -> CPD-19167 + CO-A; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadA (protein.P21151), fadI (protein.P76503). Substrates: Acetyl-CoA (molecule.C00024), (5Z)-tetradecenoyl-CoA (molecule.ecocyc.CPD-15436). Products: CoA (molecule.C00010), 3-oxo-(7Z)-hexadecenoyl-CoA (molecule.ecocyc.CPD-19167).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-15436 + ACETYL-COA -> CPD-19167 + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21151|protein.P21151]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19167|molecule.ecocyc.CPD-19167]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15436|molecule.ecocyc.CPD-15436]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17782`

## Notes

CPD-15436 + ACETYL-COA -> CPD-19167 + CO-A; direction=REVERSIBLE
