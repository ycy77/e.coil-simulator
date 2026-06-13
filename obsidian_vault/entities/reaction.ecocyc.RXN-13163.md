---
entity_id: "reaction.ecocyc.RXN-13163"
entity_type: "reaction"
name: "RXN-13163"
source_database: "EcoCyc"
source_id: "RXN-13163"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13163

`reaction.ecocyc.RXN-13163`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13163`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> 3-CARBOXY-3-HYDROXY-ISOCAPROATE; direction=REVERSIBLE EcoCyc reaction equation: 2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> 3-CARBOXY-3-HYDROXY-ISOCAPROATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by 3-isopropylmalate dehydratase (complex.ecocyc.3-ISOPROPYLMALISOM-CPLX). Substrates: (2R,3S)-3-Isopropylmalate (molecule.C04411). Products: alpha-Isopropylmalate (molecule.C02504).

## Annotation

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> 3-CARBOXY-3-HYDROXY-ISOCAPROATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.3-ISOPROPYLMALISOM-CPLX|complex.ecocyc.3-ISOPROPYLMALISOM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C02504|molecule.C02504]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04411|molecule.C04411]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-13163`

## Notes

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE -> 3-CARBOXY-3-HYDROXY-ISOCAPROATE; direction=REVERSIBLE
