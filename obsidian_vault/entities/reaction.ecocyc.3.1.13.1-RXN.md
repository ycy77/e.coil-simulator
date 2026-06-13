---
entity_id: "reaction.ecocyc.3.1.13.1-RXN"
entity_type: "reaction"
name: "3.1.13.1-RXN"
source_database: "EcoCyc"
source_id: "3.1.13.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Ribonuclease II"
---

# 3.1.13.1-RXN

`reaction.ecocyc.3.1.13.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.13.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNASE-II-DEGRADATION-SUBSTRATE-MRNA + WATER -> Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNASE-II-DEGRADATION-SUBSTRATE-MRNA + WATER -> Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rnb (protein.P30850). Substrates: H2O (molecule.C00001). Products: a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates).

## Annotation

RNASE-II-DEGRADATION-SUBSTRATE-MRNA + WATER -> Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P30850|protein.P30850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.1.13.1-RXN`

## Notes

RNASE-II-DEGRADATION-SUBSTRATE-MRNA + WATER -> Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
