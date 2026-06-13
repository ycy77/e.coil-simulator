---
entity_id: "reaction.ecocyc.THI-P-SYN-RXN"
entity_type: "reaction"
name: "THI-P-SYN-RXN"
source_database: "EcoCyc"
source_id: "THI-P-SYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THI-P-SYN-RXN

`reaction.ecocyc.THI-P-SYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THI-P-SYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the condensation step in thiamin-P synthesis. EcoCyc reaction equation: PROTON + THZ-P + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP -> THIAMINE-P + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This is the condensation step in thiamin-P synthesis.

## Biological Role

Catalyzed by thiE (protein.P30137). Substrates: H+ (molecule.C00080), 4-Methyl-5-(2-phosphooxyethyl)thiazole (molecule.C04327), 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate (molecule.C04752). Products: Diphosphate (molecule.C00013), Thiamin monophosphate (molecule.C01081).

## Enriched Pathways

- `ecocyc.PWY-6897` thiamine diphosphate salvage II (EcoCyc)

## Annotation

This is the condensation step in thiamin-P synthesis.

## Pathways

- `ecocyc.PWY-6897` thiamine diphosphate salvage II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[protein.P30137|protein.P30137]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01081|molecule.C01081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04327|molecule.C04327]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04752|molecule.C04752]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00227|molecule.C00227]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02305|molecule.C02305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THI-P-SYN-RXN`

## Notes

PROTON + THZ-P + AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP -> THIAMINE-P + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
