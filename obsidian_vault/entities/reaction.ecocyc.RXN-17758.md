---
entity_id: "reaction.ecocyc.RXN-17758"
entity_type: "reaction"
name: "RXN-17758"
source_database: "EcoCyc"
source_id: "RXN-17758"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17758

`reaction.ecocyc.RXN-17758`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17758`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BETAINE_ALDEHYDE + PROTON + E- -> CHOLINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: BETAINE_ALDEHYDE + PROTON + E- -> CHOLINE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Betaine aldehyde (molecule.C00576). Products: Choline (molecule.C00114).

## Annotation

BETAINE_ALDEHYDE + PROTON + E- -> CHOLINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00576|molecule.C00576]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17758`

## Notes

BETAINE_ALDEHYDE + PROTON + E- -> CHOLINE; direction=LEFT-TO-RIGHT
