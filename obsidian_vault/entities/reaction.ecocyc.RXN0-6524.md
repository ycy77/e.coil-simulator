---
entity_id: "reaction.ecocyc.RXN0-6524"
entity_type: "reaction"
name: "RXN0-6524"
source_database: "EcoCyc"
source_id: "RXN0-6524"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6524

`reaction.ecocyc.RXN0-6524`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6524`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNASE-II-POLY-A-SUBSTRATE-MRNA + WATER -> RNASE-II-SUBSTRATE-WITH-NO-POLY-A-TAIL + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNASE-II-POLY-A-SUBSTRATE-MRNA + WATER -> RNASE-II-SUBSTRATE-WITH-NO-POLY-A-TAIL + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rnb (protein.P30850). Substrates: H2O (molecule.C00001). Products: AMP (molecule.C00020).

## Annotation

RNASE-II-POLY-A-SUBSTRATE-MRNA + WATER -> RNASE-II-SUBSTRATE-WITH-NO-POLY-A-TAIL + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P30850|protein.P30850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6524`

## Notes

RNASE-II-POLY-A-SUBSTRATE-MRNA + WATER -> RNASE-II-SUBSTRATE-WITH-NO-POLY-A-TAIL + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
