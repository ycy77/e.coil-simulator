---
entity_id: "reaction.ecocyc.RXN0-5309"
entity_type: "reaction"
name: "RXN0-5309"
source_database: "EcoCyc"
source_id: "RXN0-5309"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5309

`reaction.ecocyc.RXN0-5309`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5309`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UBIQUINONE-8 + PROTON + E- -> CPD-9956; direction=LEFT-TO-RIGHT EcoCyc reaction equation: UBIQUINONE-8 + PROTON + E- -> CPD-9956; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), ubiquinone-8 (molecule.ecocyc.UBIQUINONE-8). Products: ubiquinol-8 (molecule.ecocyc.CPD-9956).

## Annotation

UBIQUINONE-8 + PROTON + E- -> CPD-9956; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-9956|molecule.ecocyc.CPD-9956]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.UBIQUINONE-8|molecule.ecocyc.UBIQUINONE-8]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5309`

## Notes

UBIQUINONE-8 + PROTON + E- -> CPD-9956; direction=LEFT-TO-RIGHT
