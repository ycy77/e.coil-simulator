---
entity_id: "reaction.ecocyc.RXN0-5255"
entity_type: "reaction"
name: "RXN0-5255"
source_database: "EcoCyc"
source_id: "RXN0-5255"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5255

`reaction.ecocyc.RXN0-5255`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5255`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + E- -> HYDROGEN-MOLECULE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + E- -> HYDROGEN-MOLECULE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080). Products: Hydrogen (molecule.C00282).

## Annotation

PROTON + E- -> HYDROGEN-MOLECULE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5255`

## Notes

PROTON + E- -> HYDROGEN-MOLECULE; direction=LEFT-TO-RIGHT
