---
entity_id: "reaction.ecocyc.RXN-22711"
entity_type: "reaction"
name: "RXN-22711"
source_database: "EcoCyc"
source_id: "RXN-22711"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22711

`reaction.ecocyc.RXN-22711`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22711`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CHORISMATE + AMMONIA + PROTON -> CPD-9517 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CHORISMATE + AMMONIA + PROTON -> CPD-9517 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Ammonia (molecule.C00014), H+ (molecule.C00080), Chorismate (molecule.C00251). Products: H2O (molecule.C00001), (2S)-2-amino-4-deoxy-chorismate (molecule.ecocyc.CPD-9517).

## Annotation

CHORISMATE + AMMONIA + PROTON -> CPD-9517 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9517|molecule.ecocyc.CPD-9517]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22711`

## Notes

CHORISMATE + AMMONIA + PROTON -> CPD-9517 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
