---
entity_id: "reaction.ecocyc.RXN-13329"
entity_type: "reaction"
name: "RXN-13329"
source_database: "EcoCyc"
source_id: "RXN-13329"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13329

`reaction.ecocyc.RXN-13329`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13329`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD-12279 + WATER -> GLYOX + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-12279 + WATER -> GLYOX + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Iminoglycine (molecule.C15809). Products: Glyoxylate (molecule.C00048), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

PROTON + CPD-12279 + WATER -> GLYOX + AMMONIUM; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15809|molecule.C15809]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13329`

## Notes

PROTON + CPD-12279 + WATER -> GLYOX + AMMONIUM; direction=LEFT-TO-RIGHT
