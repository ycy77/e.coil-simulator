---
entity_id: "reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN"
entity_type: "reaction"
name: "2-METHYLCITRATE-DEHYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "2-METHYLCITRATE-DEHYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-METHYLCITRATE-DEHYDRATASE-RXN

`reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-METHYLCITRATE-DEHYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant . EcoCyc reaction equation: CPD-622 -> WATER + CPD-1136; direction=LEFT-TO-RIGHT. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant .

## Biological Role

Catalyzed by prpD (protein.P77243). Substrates: (2S,3S)-2-methylcitrate (molecule.ecocyc.CPD-622). Products: H2O (molecule.C00001), (Z)-But-2-ene-1,2,3-tricarboxylate (molecule.C04225).

## Enriched Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Annotation

The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant .

## Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77243|protein.P77243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04225|molecule.C04225]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-622|molecule.ecocyc.CPD-622]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2-METHYLCITRATE-DEHYDRATASE-RXN`

## Notes

CPD-622 -> WATER + CPD-1136; direction=LEFT-TO-RIGHT
