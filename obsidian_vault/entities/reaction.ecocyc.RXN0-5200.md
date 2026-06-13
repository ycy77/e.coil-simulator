---
entity_id: "reaction.ecocyc.RXN0-5200"
entity_type: "reaction"
name: "RXN0-5200"
source_database: "EcoCyc"
source_id: "RXN0-5200"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5200

`reaction.ecocyc.RXN0-5200`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5200`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Aminated-Amine-Donors + 2-OXOBUTANOATE -> CPD0-1942 + Deaminated-Amine-Donors; direction=REVERSIBLE EcoCyc reaction equation: Aminated-Amine-Donors + 2-OXOBUTANOATE -> CPD0-1942 + Deaminated-Amine-Donors; direction=REVERSIBLE.

## Biological Role

Catalyzed by avtA (protein.P09053). Substrates: 2-Oxobutanoate (molecule.C00109), an aminated amino group donor (molecule.ecocyc.Aminated-Amine-Donors). Products: (S)-2-Aminobutanoate (molecule.C02356), a deaminated amino group donor (molecule.ecocyc.Deaminated-Amine-Donors).

## Annotation

Aminated-Amine-Donors + 2-OXOBUTANOATE -> CPD0-1942 + Deaminated-Amine-Donors; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P09053|protein.P09053]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C02356|molecule.C02356]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Deaminated-Amine-Donors|molecule.ecocyc.Deaminated-Amine-Donors]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aminated-Amine-Donors|molecule.ecocyc.Aminated-Amine-Donors]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5200`

## Notes

Aminated-Amine-Donors + 2-OXOBUTANOATE -> CPD0-1942 + Deaminated-Amine-Donors; direction=REVERSIBLE
