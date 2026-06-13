---
entity_id: "reaction.ecocyc.RXN0-7367"
entity_type: "reaction"
name: "RXN0-7367"
source_database: "EcoCyc"
source_id: "RXN0-7367"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7367

`reaction.ecocyc.RXN0-7367`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7367`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1122 -> CPD-6182 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1122 -> CPD-6182 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by KpLE2 phage-like element; 2,7-anhydro-N-acetylneuraminate hydratase (complex.ecocyc.CPLX0-8544). Substrates: N-acetyl-α-neuraminate (molecule.ecocyc.CPD0-1122). Products: H2O (molecule.C00001), 2,7-anhydro-α-N-acetylneuraminate (molecule.ecocyc.CPD-6182).

## Annotation

CPD0-1122 -> CPD-6182 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8544|complex.ecocyc.CPLX0-8544]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-6182|molecule.ecocyc.CPD-6182]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1122|molecule.ecocyc.CPD0-1122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7367`

## Notes

CPD0-1122 -> CPD-6182 + WATER; direction=REVERSIBLE
