---
entity_id: "reaction.ecocyc.IPPISOM-RXN"
entity_type: "reaction"
name: "IPPISOM-RXN"
source_database: "EcoCyc"
source_id: "IPPISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Isopentenyl pyrophosphate isomerase"
  - "IPP isomerase"
---

# IPPISOM-RXN

`reaction.ecocyc.IPPISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:IPPISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the biosynthesis of polyisoprenoids. EcoCyc reaction equation: DELTA3-ISOPENTENYL-PP -> CPD-4211; direction=REVERSIBLE. This is the first reaction in the biosynthesis of polyisoprenoids.

## Biological Role

Catalyzed by idi (protein.Q46822). Substrates: Isopentenyl diphosphate (molecule.C00129). Products: Dimethylallyl diphosphate (molecule.C00235).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

This is the first reaction in the biosynthesis of polyisoprenoids.

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q46822|protein.Q46822]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00235|molecule.C00235]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00129|molecule.C00129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1025|molecule.ecocyc.CPD0-1025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:IPPISOM-RXN`

## Notes

DELTA3-ISOPENTENYL-PP -> CPD-4211; direction=REVERSIBLE
