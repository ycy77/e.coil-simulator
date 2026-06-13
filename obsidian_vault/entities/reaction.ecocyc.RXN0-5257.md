---
entity_id: "reaction.ecocyc.RXN0-5257"
entity_type: "reaction"
name: "RXN0-5257"
source_database: "EcoCyc"
source_id: "RXN0-5257"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5257

`reaction.ecocyc.RXN0-5257`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5257`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXY-ACETONE-PHOSPHATE + PROTON + E- -> GLYCEROL-3P; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXY-ACETONE-PHOSPHATE + PROTON + E- -> GLYCEROL-3P; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Glycerone phosphate (molecule.C00111). Products: sn-Glycerol 3-phosphate (molecule.C00093).

## Annotation

DIHYDROXY-ACETONE-PHOSPHATE + PROTON + E- -> GLYCEROL-3P; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5257`

## Notes

DIHYDROXY-ACETONE-PHOSPHATE + PROTON + E- -> GLYCEROL-3P; direction=LEFT-TO-RIGHT
