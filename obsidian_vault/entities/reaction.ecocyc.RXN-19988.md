---
entity_id: "reaction.ecocyc.RXN-19988"
entity_type: "reaction"
name: "RXN-19988"
source_database: "EcoCyc"
source_id: "RXN-19988"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19988

`reaction.ecocyc.RXN-19988`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19988`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DISULFOXRED-MONOMER + UBIQUINONE-8 -> MONOMER0-4152 + CPD-9956; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DISULFOXRED-MONOMER + UBIQUINONE-8 -> MONOMER0-4152 + CPD-9956; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dsbB (protein.P0A6M2). Substrates: ubiquinone-8 (molecule.ecocyc.UBIQUINONE-8). Products: ubiquinol-8 (molecule.ecocyc.CPD-9956).

## Annotation

DISULFOXRED-MONOMER + UBIQUINONE-8 -> MONOMER0-4152 + CPD-9956; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A6M2|protein.P0A6M2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-9956|molecule.ecocyc.CPD-9956]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.UBIQUINONE-8|molecule.ecocyc.UBIQUINONE-8]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19988`

## Notes

DISULFOXRED-MONOMER + UBIQUINONE-8 -> MONOMER0-4152 + CPD-9956; direction=PHYSIOL-LEFT-TO-RIGHT
