---
entity_id: "reaction.ecocyc.RXN-20708"
entity_type: "reaction"
name: "RXN-20708"
source_database: "EcoCyc"
source_id: "RXN-20708"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20708

`reaction.ecocyc.RXN-20708`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20708`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THYMINE + CPD-24463 -> CPD-22331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THYMINE + CPD-24463 -> CPD-22331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Thymine (molecule.C00178), FMN-N5-peroxide (molecule.ecocyc.CPD-24463). Products: FMN-N5-oxide (molecule.ecocyc.CPD-22329), (Z)-2-methylureidoacrylate (molecule.ecocyc.CPD-22331).

## Annotation

THYMINE + CPD-24463 -> CPD-22331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.CPD-22329|molecule.ecocyc.CPD-22329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22331|molecule.ecocyc.CPD-22331]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24463|molecule.ecocyc.CPD-24463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20708`

## Notes

THYMINE + CPD-24463 -> CPD-22331 + CPD-22329; direction=PHYSIOL-LEFT-TO-RIGHT
