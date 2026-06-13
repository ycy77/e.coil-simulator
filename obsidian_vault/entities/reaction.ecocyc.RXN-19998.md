---
entity_id: "reaction.ecocyc.RXN-19998"
entity_type: "reaction"
name: "RXN-19998"
source_database: "EcoCyc"
source_id: "RXN-19998"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19998

`reaction.ecocyc.RXN-19998`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19998`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DISULFOXRED-MONOMER + CPD-9728 -> MONOMER0-4152 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DISULFOXRED-MONOMER + CPD-9728 -> MONOMER0-4152 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dsbB (protein.P0A6M2). Substrates: menaquinone-8 (molecule.ecocyc.CPD-9728). Products: menaquinol-8 (molecule.ecocyc.REDUCED-MENAQUINONE).

## Annotation

DISULFOXRED-MONOMER + CPD-9728 -> MONOMER0-4152 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A6M2|protein.P0A6M2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.REDUCED-MENAQUINONE|molecule.ecocyc.REDUCED-MENAQUINONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9728|molecule.ecocyc.CPD-9728]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19998`

## Notes

DISULFOXRED-MONOMER + CPD-9728 -> MONOMER0-4152 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT
