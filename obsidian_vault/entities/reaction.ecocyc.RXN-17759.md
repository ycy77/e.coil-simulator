---
entity_id: "reaction.ecocyc.RXN-17759"
entity_type: "reaction"
name: "RXN-17759"
source_database: "EcoCyc"
source_id: "RXN-17759"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17759

`reaction.ecocyc.RXN-17759`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17759`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BETAINE + PROTON + E- -> BETAINE-ALDEHYDE-HYDRATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: BETAINE + PROTON + E- -> BETAINE-ALDEHYDE-HYDRATE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Betaine (molecule.C00719). Products: betaine aldehyde hydrate (molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE).

## Annotation

BETAINE + PROTON + E- -> BETAINE-ALDEHYDE-HYDRATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE|molecule.ecocyc.BETAINE-ALDEHYDE-HYDRATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17759`

## Notes

BETAINE + PROTON + E- -> BETAINE-ALDEHYDE-HYDRATE; direction=LEFT-TO-RIGHT
