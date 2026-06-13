---
entity_id: "reaction.ecocyc.RXN0-7391"
entity_type: "reaction"
name: "RXN0-7391"
source_database: "EcoCyc"
source_id: "RXN0-7391"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7391

`reaction.ecocyc.RXN0-7391`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7391`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIACETYLCHITOBIOSE-6-PHOSPHATE + WATER -> CPD0-2705 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIACETYLCHITOBIOSE-6-PHOSPHATE + WATER -> CPD0-2705 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by chbG (protein.P37794). Substrates: H2O (molecule.C00001), N,N'-Diacetylchitobiose 6'-phosphate (molecule.C21152). Products: Acetate (molecule.C00033), 6-phospho-β-D-glucosaminyl-(1->4)-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-2705).

## Enriched Pathways

- `ecocyc.PWY0-1309` chitobiose degradation (EcoCyc)

## Annotation

DIACETYLCHITOBIOSE-6-PHOSPHATE + WATER -> CPD0-2705 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1309` chitobiose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37794|protein.P37794]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2705|molecule.ecocyc.CPD0-2705]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C21152|molecule.C21152]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7391`

## Notes

DIACETYLCHITOBIOSE-6-PHOSPHATE + WATER -> CPD0-2705 + ACET; direction=PHYSIOL-LEFT-TO-RIGHT
