---
entity_id: "reaction.ecocyc.RXN-8991"
entity_type: "reaction"
name: "3-isopropylmalate dehydratase"
source_database: "EcoCyc"
source_id: "RXN-8991"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "&alpha"
  - "-IPM isomerase"
  - "Isopropylmalate isomerase"
---

# 3-isopropylmalate dehydratase

`reaction.ecocyc.RXN-8991`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8991`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> CPD-9451 + WATER; direction=REVERSIBLE EcoCyc reaction equation: 2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> CPD-9451 + WATER; direction=REVERSIBLE.

## Biological Role

Substrates: (2R,3S)-3-Isopropylmalate (molecule.C04411). Products: H2O (molecule.C00001), 2-Isopropylmaleate (molecule.C02631).

## Enriched Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Annotation

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> CPD-9451 + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02631|molecule.C02631]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04411|molecule.C04411]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8991`

## Notes

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> CPD-9451 + WATER; direction=REVERSIBLE
