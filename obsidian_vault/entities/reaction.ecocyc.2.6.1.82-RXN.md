---
entity_id: "reaction.ecocyc.2.6.1.82-RXN"
entity_type: "reaction"
name: "2.6.1.82-RXN"
source_database: "EcoCyc"
source_id: "2.6.1.82-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.6.1.82-RXN

`reaction.ecocyc.2.6.1.82-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.6.1.82-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PUTRESCINE + 2-KETOGLUTARATE -> GLT + CPD-6124 + WATER; direction=REVERSIBLE EcoCyc reaction equation: PUTRESCINE + 2-KETOGLUTARATE -> GLT + CPD-6124 + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: 2-Oxoglutarate (molecule.C00026), Putrescine (molecule.C00134). Products: H2O (molecule.C00001), L-Glutamate (molecule.C00025), 1-pyrroline (molecule.ecocyc.CPD-6124).

## Annotation

PUTRESCINE + 2-KETOGLUTARATE -> GLT + CPD-6124 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-6124|molecule.ecocyc.CPD-6124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.6.1.82-RXN`

## Notes

PUTRESCINE + 2-KETOGLUTARATE -> GLT + CPD-6124 + WATER; direction=REVERSIBLE
