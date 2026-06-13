---
entity_id: "reaction.ecocyc.PHOSPHOAMIDASE-RXN"
entity_type: "reaction"
name: "PHOSPHOAMIDASE-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHOAMIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHOAMIDASE-RXN

`reaction.ecocyc.PHOSPHOAMIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHOAMIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WATER + CREATINE-P -> Pi + CREATINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + CREATINE-P -> Pi + CREATINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Phosphocreatine (molecule.C02305). Products: Creatine (molecule.C00300), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + CREATINE-P -> Pi + CREATINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00300|molecule.C00300]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02305|molecule.C02305]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOSPHOAMIDASE-RXN`

## Notes

WATER + CREATINE-P -> Pi + CREATINE; direction=PHYSIOL-LEFT-TO-RIGHT
