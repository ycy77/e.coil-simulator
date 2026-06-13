---
entity_id: "reaction.ecocyc.RXN0-4641"
entity_type: "reaction"
name: "RXN0-4641"
source_database: "EcoCyc"
source_id: "RXN0-4641"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4641

`reaction.ecocyc.RXN0-4641`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4641`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-881 + WATER -> N-ACETYL-D-GLUCOSAMINE-6-P + D-LACTATE; direction=REVERSIBLE EcoCyc reaction equation: CPD0-881 + WATER -> N-ACETYL-D-GLUCOSAMINE-6-P + D-LACTATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by N-acetylmuramic acid 6-phosphate etherase (complex.ecocyc.CPLX0-7732). Substrates: H2O (molecule.C00001), N-Acetylmuramic acid 6-phosphate (molecule.C16698). Products: (R)-Lactate (molecule.C00256), N-Acetyl-D-glucosamine 6-phosphate (molecule.C00357).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

CPD0-881 + WATER -> N-ACETYL-D-GLUCOSAMINE-6-P + D-LACTATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7732|complex.ecocyc.CPLX0-7732]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16698|molecule.C16698]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4641`

## Notes

CPD0-881 + WATER -> N-ACETYL-D-GLUCOSAMINE-6-P + D-LACTATE; direction=REVERSIBLE
