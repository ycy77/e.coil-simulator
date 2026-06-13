---
entity_id: "reaction.ecocyc.GPPSYN-RXN"
entity_type: "reaction"
name: "GPPSYN-RXN"
source_database: "EcoCyc"
source_id: "GPPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Geranyl-diphosphate synthase"
  - "Prenyltransferase"
---

# GPPSYN-RXN

`reaction.ecocyc.GPPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GPPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the biosynthesis of polyisoprenoids. EcoCyc reaction equation: CPD-4211 + DELTA3-ISOPENTENYL-PP -> GERANYL-PP + PPI; direction=LEFT-TO-RIGHT. This is the second reaction in the biosynthesis of polyisoprenoids.

## Biological Role

Catalyzed by ispA (protein.P22939). Substrates: Isopentenyl diphosphate (molecule.C00129), Dimethylallyl diphosphate (molecule.C00235). Products: Diphosphate (molecule.C00013), Geranyl diphosphate (molecule.C00341).

## Enriched Pathways

- `ecocyc.PWY-5123` trans, trans-farnesyl diphosphate biosynthesis (EcoCyc)

## Annotation

This is the second reaction in the biosynthesis of polyisoprenoids.

## Pathways

- `ecocyc.PWY-5123` trans, trans-farnesyl diphosphate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P22939|protein.P22939]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00341|molecule.C00341]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00129|molecule.C00129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00235|molecule.C00235]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GPPSYN-RXN`

## Notes

CPD-4211 + DELTA3-ISOPENTENYL-PP -> GERANYL-PP + PPI; direction=LEFT-TO-RIGHT
