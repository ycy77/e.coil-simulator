---
entity_id: "reaction.ecocyc.RXN0-6435"
entity_type: "reaction"
name: "HypF carbamoyltransferase"
source_database: "EcoCyc"
source_id: "RXN0-6435"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HypF carbamoyltransferase

`reaction.ecocyc.RXN0-6435`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6435`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARBAMOYL-P + HypE-Proteins + ATP + WATER -> HypE-S-carboxamide + AMP + PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CARBAMOYL-P + HypE-Proteins + ATP + WATER -> HypE-S-carboxamide + AMP + PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hypF (protein.P30131). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Carbamoyl phosphate (molecule.C00169). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Annotation

CARBAMOYL-P + HypE-Proteins + ATP + WATER -> HypE-S-carboxamide + AMP + PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P30131|protein.P30131]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6435`

## Notes

CARBAMOYL-P + HypE-Proteins + ATP + WATER -> HypE-S-carboxamide + AMP + PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
