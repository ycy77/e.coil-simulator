---
entity_id: "reaction.ecocyc.RXN0-5262"
entity_type: "reaction"
name: "RXN0-5262"
source_database: "EcoCyc"
source_id: "RXN0-5262"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5262

`reaction.ecocyc.RXN0-5262`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5262`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DMSO + PROTON + E- -> CPD-7670 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DMSO + PROTON + E- -> CPD-7670 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Dimethyl sulfoxide (molecule.C11143). Products: H2O (molecule.C00001), Dimethyl sulfide (molecule.C00580).

## Annotation

DMSO + PROTON + E- -> CPD-7670 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00580|molecule.C00580]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11143|molecule.C11143]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5262`

## Notes

DMSO + PROTON + E- -> CPD-7670 + WATER; direction=LEFT-TO-RIGHT
