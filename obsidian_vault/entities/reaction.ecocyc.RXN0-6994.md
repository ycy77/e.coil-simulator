---
entity_id: "reaction.ecocyc.RXN0-6994"
entity_type: "reaction"
name: "RXN0-6994"
source_database: "EcoCyc"
source_id: "RXN0-6994"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6994

`reaction.ecocyc.RXN0-6994`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6994`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2499 + WATER -> GLC-6-P + METOH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2499 + WATER -> GLC-6-P + METOH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bglA (protein.Q46829). Substrates: H2O (molecule.C00001), methyl β-D-glucoside 6-phosphate (molecule.ecocyc.CPD0-2499). Products: Methanol (molecule.C00132), beta-D-Glucose 6-phosphate (molecule.C01172).

## Annotation

CPD0-2499 + WATER -> GLC-6-P + METOH; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q46829|protein.Q46829]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2499|molecule.ecocyc.CPD0-2499]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6994`

## Notes

CPD0-2499 + WATER -> GLC-6-P + METOH; direction=PHYSIOL-LEFT-TO-RIGHT
