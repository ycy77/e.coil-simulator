---
entity_id: "reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN"
entity_type: "reaction"
name: "3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN

`reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-650 -> WATER + CROTONYL-COA; direction=REVERSIBLE EcoCyc reaction equation: CPD-650 -> WATER + CROTONYL-COA; direction=REVERSIBLE.

## Biological Role

Catalyzed by oxepin-CoA hydrolase [multifunctional] (complex.ecocyc.CPLX0-8538). Substrates: (R)-3-Hydroxybutanoyl-CoA (molecule.C03561). Products: H2O (molecule.C00001), Crotonoyl-CoA (molecule.C00877).

## Annotation

CPD-650 -> WATER + CROTONYL-COA; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8538|complex.ecocyc.CPLX0-8538]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00877|molecule.C00877]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03561|molecule.C03561]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN`

## Notes

CPD-650 -> WATER + CROTONYL-COA; direction=REVERSIBLE
