---
entity_id: "reaction.ecocyc.RXN-21027"
entity_type: "reaction"
name: "RXN-21027"
source_database: "EcoCyc"
source_id: "RXN-21027"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21027

`reaction.ecocyc.RXN-21027`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21027`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ArsC-S-As-OH + WATER -> Arsenate-Reductase-Cysteines + CPD-763 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ArsC-S-As-OH + WATER -> Arsenate-Reductase-Cysteines + CPD-763 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), S-arsorososulfanethiol-[arsenate reductase] (molecule.ecocyc.ArsC-S-As-OH). Products: H+ (molecule.C00080), an [arsenate reductase]-L-cysteine (molecule.ecocyc.Arsenate-Reductase-Cysteines), arsenite (molecule.ecocyc.CPD-763).

## Annotation

ArsC-S-As-OH + WATER -> Arsenate-Reductase-Cysteines + CPD-763 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Arsenate-Reductase-Cysteines|molecule.ecocyc.Arsenate-Reductase-Cysteines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ArsC-S-As-OH|molecule.ecocyc.ArsC-S-As-OH]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21027`

## Notes

ArsC-S-As-OH + WATER -> Arsenate-Reductase-Cysteines + CPD-763 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
