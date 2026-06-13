---
entity_id: "reaction.ecocyc.2.6.1.7-RXN"
entity_type: "reaction"
name: "2.6.1.7-RXN"
source_database: "EcoCyc"
source_id: "2.6.1.7-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Kynurenine aminotransferase"
---

# 2.6.1.7-RXN

`reaction.ecocyc.2.6.1.7-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.6.1.7-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14736 + 2-KETOGLUTARATE -> GLT + CPD-476; direction=REVERSIBLE EcoCyc reaction equation: CPD-14736 + 2-KETOGLUTARATE -> GLT + CPD-476; direction=REVERSIBLE.

## Biological Role

Substrates: 2-Oxoglutarate (molecule.C00026), L-Kynurenine (molecule.C00328). Products: L-Glutamate (molecule.C00025), 4-(2-Aminophenyl)-2,4-dioxobutanoate (molecule.C01252).

## Annotation

CPD-14736 + 2-KETOGLUTARATE -> GLT + CPD-476; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01252|molecule.C01252]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00328|molecule.C00328]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.6.1.7-RXN`

## Notes

CPD-14736 + 2-KETOGLUTARATE -> GLT + CPD-476; direction=REVERSIBLE
