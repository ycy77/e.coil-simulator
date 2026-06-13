---
entity_id: "reaction.ecocyc.RXN-18550"
entity_type: "reaction"
name: "RXN-18550"
source_database: "EcoCyc"
source_id: "RXN-18550"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18550

`reaction.ecocyc.RXN-18550`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18550`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DSBBPROT-MONOMER + CPD-9728 -> MONOMER0-4142 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DSBBPROT-MONOMER + CPD-9728 -> MONOMER0-4142 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: menaquinone-8 (molecule.ecocyc.CPD-9728). Products: menaquinol-8 (molecule.ecocyc.REDUCED-MENAQUINONE).

## Annotation

DSBBPROT-MONOMER + CPD-9728 -> MONOMER0-4142 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.REDUCED-MENAQUINONE|molecule.ecocyc.REDUCED-MENAQUINONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9728|molecule.ecocyc.CPD-9728]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18550`

## Notes

DSBBPROT-MONOMER + CPD-9728 -> MONOMER0-4142 + REDUCED-MENAQUINONE; direction=PHYSIOL-LEFT-TO-RIGHT
