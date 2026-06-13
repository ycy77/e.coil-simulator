---
entity_id: "reaction.ecocyc.TRE6PHYDRO-RXN"
entity_type: "reaction"
name: "TRE6PHYDRO-RXN"
source_database: "EcoCyc"
source_id: "TRE6PHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRE6PHYDRO-RXN

`reaction.ecocyc.TRE6PHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRE6PHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TREHALOSE-6P + WATER -> D-glucopyranose-6-phosphate + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TREHALOSE-6P + WATER -> D-glucopyranose-6-phosphate + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by treC (protein.P28904). Substrates: H2O (molecule.C00001), alpha,alpha'-Trehalose 6-phosphate (molecule.C00689). Products: D-Glucose (molecule.C00031), D-Glucose 6-phosphate (molecule.C00092).

## Enriched Pathways

- `ecocyc.TREDEGLOW-PWY` trehalose degradation I (low osmolarity) (EcoCyc)

## Annotation

TREHALOSE-6P + WATER -> D-glucopyranose-6-phosphate + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TREDEGLOW-PWY` trehalose degradation I (low osmolarity) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P28904|protein.P28904]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00689|molecule.C00689]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRE6PHYDRO-RXN`

## Notes

TREHALOSE-6P + WATER -> D-glucopyranose-6-phosphate + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
