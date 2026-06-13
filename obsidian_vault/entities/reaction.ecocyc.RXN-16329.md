---
entity_id: "reaction.ecocyc.RXN-16329"
entity_type: "reaction"
name: "RXN-16329"
source_database: "EcoCyc"
source_id: "RXN-16329"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16329

`reaction.ecocyc.RXN-16329`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16329`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXALACETIC_ACID + PROTON + E- -> MAL; direction=LEFT-TO-RIGHT EcoCyc reaction equation: OXALACETIC_ACID + PROTON + E- -> MAL; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxaloacetate (molecule.C00036), H+ (molecule.C00080). Products: (S)-Malate (molecule.C00149).

## Annotation

OXALACETIC_ACID + PROTON + E- -> MAL; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16329`

## Notes

OXALACETIC_ACID + PROTON + E- -> MAL; direction=LEFT-TO-RIGHT
