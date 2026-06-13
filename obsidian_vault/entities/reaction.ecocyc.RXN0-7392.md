---
entity_id: "reaction.ecocyc.RXN0-7392"
entity_type: "reaction"
name: "RXN0-7392"
source_database: "EcoCyc"
source_id: "RXN0-7392"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7392

`reaction.ecocyc.RXN0-7392`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7392`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2705 + WATER -> D-GLUCOSAMINE-6-P + N-acetyl-D-glucosamine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2705 + WATER -> D-GLUCOSAMINE-6-P + N-acetyl-D-glucosamine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by monoacetylchitobiose-6-phosphate hydrolase (complex.ecocyc.CPLX0-7979). Substrates: H2O (molecule.C00001), 6-phospho-β-D-glucosaminyl-(1->4)-N-acetyl-D-glucosamine (molecule.ecocyc.CPD0-2705). Products: N-Acetyl-D-glucosamine (molecule.C00140), D-Glucosamine 6-phosphate (molecule.C00352).

## Enriched Pathways

- `ecocyc.PWY0-1309` chitobiose degradation (EcoCyc)

## Annotation

CPD0-2705 + WATER -> D-GLUCOSAMINE-6-P + N-acetyl-D-glucosamine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1309` chitobiose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7979|complex.ecocyc.CPLX0-7979]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00140|molecule.C00140]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2705|molecule.ecocyc.CPD0-2705]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7392`

## Notes

CPD0-2705 + WATER -> D-GLUCOSAMINE-6-P + N-acetyl-D-glucosamine; direction=PHYSIOL-LEFT-TO-RIGHT
