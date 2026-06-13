---
entity_id: "reaction.ecocyc.RXN-25372"
entity_type: "reaction"
name: "RXN-25372"
source_database: "EcoCyc"
source_id: "RXN-25372"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25372

`reaction.ecocyc.RXN-25372`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25372`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMMONIA + CPD-27984 -> AMP + CPD-27985 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: AMMONIA + CPD-27984 -> AMP + CPD-27985 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Ammonia (molecule.C00014), 7-carboxyadenylyl-7-carbaguanine (molecule.ecocyc.CPD-27984). Products: AMP (molecule.C00020), H+ (molecule.C00080), 7-amido-7-carbaguanine (molecule.ecocyc.CPD-27985).

## Annotation

AMMONIA + CPD-27984 -> AMP + CPD-27985 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-27985|molecule.ecocyc.CPD-27985]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27984|molecule.ecocyc.CPD-27984]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25372`

## Notes

AMMONIA + CPD-27984 -> AMP + CPD-27985 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
