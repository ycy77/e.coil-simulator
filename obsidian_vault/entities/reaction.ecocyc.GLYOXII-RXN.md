---
entity_id: "reaction.ecocyc.GLYOXII-RXN"
entity_type: "reaction"
name: "GLYOXII-RXN"
source_database: "EcoCyc"
source_id: "GLYOXII-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Glyoxalase II"
---

# GLYOXII-RXN

`reaction.ecocyc.GLYOXII-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYOXII-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of one path for the degradation of methylglyoxal. EcoCyc reaction equation: S-LACTOYL-GLUTATHIONE + WATER -> PROTON + GLUTATHIONE + D-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of one path for the degradation of methylglyoxal.

## Biological Role

Catalyzed by S-formylglutathione hydrolase / S-lactoylglutathione hydrolase (complex.ecocyc.CPLX0-3954), gloB (protein.P0AC84), gloC (protein.P75849). Substrates: H2O (molecule.C00001), (R)-S-Lactoylglutathione (molecule.C03451). Products: Glutathione (molecule.C00051), H+ (molecule.C00080), (R)-Lactate (molecule.C00256).

## Enriched Pathways

- `ecocyc.PWY-5386` methylglyoxal degradation I (EcoCyc)

## Annotation

This reaction is part of one path for the degradation of methylglyoxal.

## Pathways

- `ecocyc.PWY-5386` methylglyoxal degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3954|complex.ecocyc.CPLX0-3954]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AC84|protein.P0AC84]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75849|protein.P75849]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03451|molecule.C03451]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYOXII-RXN`

## Notes

S-LACTOYL-GLUTATHIONE + WATER -> PROTON + GLUTATHIONE + D-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT
