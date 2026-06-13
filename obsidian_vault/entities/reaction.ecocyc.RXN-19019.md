---
entity_id: "reaction.ecocyc.RXN-19019"
entity_type: "reaction"
name: "RXN-19019"
source_database: "EcoCyc"
source_id: "RXN-19019"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19019

`reaction.ecocyc.RXN-19019`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19019`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROGEN-PEROXIDE + PROTON + E- -> WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: HYDROGEN-PEROXIDE + PROTON + E- -> WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), H+ (molecule.C00080). Products: H2O (molecule.C00001).

## Annotation

HYDROGEN-PEROXIDE + PROTON + E- -> WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19019`

## Notes

HYDROGEN-PEROXIDE + PROTON + E- -> WATER; direction=LEFT-TO-RIGHT
