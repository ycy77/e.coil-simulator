---
entity_id: "reaction.ecocyc.RXN-22729"
entity_type: "reaction"
name: "RXN-22729"
source_database: "EcoCyc"
source_id: "RXN-22729"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22729

`reaction.ecocyc.RXN-22729`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22729`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9517 -> ANTHRANILATE + PYRUVATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9517 -> ANTHRANILATE + PYRUVATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (2S)-2-amino-4-deoxy-chorismate (molecule.ecocyc.CPD-9517). Products: Pyruvate (molecule.C00022), H+ (molecule.C00080), Anthranilate (molecule.C00108).

## Annotation

CPD-9517 -> ANTHRANILATE + PYRUVATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00108|molecule.C00108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9517|molecule.ecocyc.CPD-9517]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22729`

## Notes

CPD-9517 -> ANTHRANILATE + PYRUVATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
