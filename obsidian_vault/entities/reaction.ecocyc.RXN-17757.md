---
entity_id: "reaction.ecocyc.RXN-17757"
entity_type: "reaction"
name: "RXN-17757"
source_database: "EcoCyc"
source_id: "RXN-17757"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17757

`reaction.ecocyc.RXN-17757`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17757`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYOX + PROTON + E- -> GLYCOLLATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GLYOX + PROTON + E- -> GLYCOLLATE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Glyoxylate (molecule.C00048), H+ (molecule.C00080). Products: Glycolate (molecule.C00160).

## Annotation

GLYOX + PROTON + E- -> GLYCOLLATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17757`

## Notes

GLYOX + PROTON + E- -> GLYCOLLATE; direction=LEFT-TO-RIGHT
