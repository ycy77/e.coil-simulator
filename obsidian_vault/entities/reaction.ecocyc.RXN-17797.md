---
entity_id: "reaction.ecocyc.RXN-17797"
entity_type: "reaction"
name: "RXN-17797"
source_database: "EcoCyc"
source_id: "RXN-17797"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17797

`reaction.ecocyc.RXN-17797`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17797`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19151 -> CPD-19150 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-19151 -> CPD-19150 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: (S)-3-hydroxy-(5Z)-dodecenoyl-CoA (molecule.ecocyc.CPD-19151). Products: H2O (molecule.C00001), (2E,5Z)-dodec-2,5-dienoyl-CoA (molecule.ecocyc.CPD-19150).

## Annotation

CPD-19151 -> CPD-19150 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19150|molecule.ecocyc.CPD-19150]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19151|molecule.ecocyc.CPD-19151]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17797`

## Notes

CPD-19151 -> CPD-19150 + WATER; direction=REVERSIBLE
