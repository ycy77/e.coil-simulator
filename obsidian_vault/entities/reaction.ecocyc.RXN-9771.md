---
entity_id: "reaction.ecocyc.RXN-9771"
entity_type: "reaction"
name: "RXN-9771"
source_database: "EcoCyc"
source_id: "RXN-9771"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9771

`reaction.ecocyc.RXN-9771`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9771`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + IMINOASPARTATE + WATER -> OXALACETIC_ACID + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + IMINOASPARTATE + WATER -> OXALACETIC_ACID + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Iminoaspartate (molecule.C05840). Products: Oxaloacetate (molecule.C00036), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

PROTON + IMINOASPARTATE + WATER -> OXALACETIC_ACID + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05840|molecule.C05840]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9771`

## Notes

PROTON + IMINOASPARTATE + WATER -> OXALACETIC_ACID + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
