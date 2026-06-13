---
entity_id: "reaction.ecocyc.RXN0-7283"
entity_type: "reaction"
name: "RXN0-7283"
source_database: "EcoCyc"
source_id: "RXN0-7283"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7283

`reaction.ecocyc.RXN0-7283`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7283`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

mRNAs-with-5-diphosphate + WATER -> mRNAs-with-5-monophosphate + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: mRNAs-with-5-diphosphate + WATER -> mRNAs-with-5-monophosphate + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rppH (protein.P0A776). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

mRNAs-with-5-diphosphate + WATER -> mRNAs-with-5-monophosphate + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A776|protein.P0A776]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7283`

## Notes

mRNAs-with-5-diphosphate + WATER -> mRNAs-with-5-monophosphate + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
