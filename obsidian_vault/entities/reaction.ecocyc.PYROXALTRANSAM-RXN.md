---
entity_id: "reaction.ecocyc.PYROXALTRANSAM-RXN"
entity_type: "reaction"
name: "PYROXALTRANSAM-RXN"
source_database: "EcoCyc"
source_id: "PYROXALTRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYROXALTRANSAM-RXN

`reaction.ecocyc.PYROXALTRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYROXALTRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

For some transamination reactions, the prosthetic group of transaminases, pyridoxal, is converted to pyridoxamine. EcoCyc reaction equation: PYRIDOXAMINE + OXALACETIC_ACID -> PYRIDOXAL + L-ASPARTATE; direction=REVERSIBLE. For some transamination reactions, the prosthetic group of transaminases, pyridoxal, is converted to pyridoxamine.

## Biological Role

Catalyzed by PYROXALTRANSAM-MONOMER (protein.ecocyc.PYROXALTRANSAM-MONOMER). Substrates: Oxaloacetate (molecule.C00036), Pyridoxamine (molecule.C00534). Products: L-Aspartate (molecule.C00049), Pyridoxal (molecule.C00250).

## Annotation

For some transamination reactions, the prosthetic group of transaminases, pyridoxal, is converted to pyridoxamine.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.ecocyc.PYROXALTRANSAM-MONOMER|protein.ecocyc.PYROXALTRANSAM-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00534|molecule.C00534]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00647|molecule.C00647]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYROXALTRANSAM-RXN`

## Notes

PYRIDOXAMINE + OXALACETIC_ACID -> PYRIDOXAL + L-ASPARTATE; direction=REVERSIBLE
