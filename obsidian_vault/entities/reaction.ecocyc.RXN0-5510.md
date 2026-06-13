---
entity_id: "reaction.ecocyc.RXN0-5510"
entity_type: "reaction"
name: "RXN0-5510"
source_database: "EcoCyc"
source_id: "RXN0-5510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5510

`reaction.ecocyc.RXN0-5510`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5510`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

mRNAs-with-5-triphosphate + WATER -> mRNAs-with-5-monophosphate + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: mRNAs-with-5-triphosphate + WATER -> mRNAs-with-5-monophosphate + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rppH (protein.P0A776). Substrates: H2O (molecule.C00001). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080).

## Annotation

mRNAs-with-5-triphosphate + WATER -> mRNAs-with-5-monophosphate + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A776|protein.P0A776]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5510`

## Notes

mRNAs-with-5-triphosphate + WATER -> mRNAs-with-5-monophosphate + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
