---
entity_id: "reaction.ecocyc.RXN-12861"
entity_type: "reaction"
name: "dehydroascorbate hydrolase"
source_database: "EcoCyc"
source_id: "RXN-12861"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# dehydroascorbate hydrolase

`reaction.ecocyc.RXN-12861`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12861`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13907 -> CPD-334 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13907 -> CPD-334 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: dehydroascorbate (bicyclic form) (molecule.ecocyc.CPD-13907). Products: H+ (molecule.C00080), 2,3-didehydro-L-gulonate (molecule.ecocyc.CPD-334).

## Annotation

CPD-13907 -> CPD-334 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-334|molecule.ecocyc.CPD-334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13907|molecule.ecocyc.CPD-13907]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12861`

## Notes

CPD-13907 -> CPD-334 + PROTON; direction=LEFT-TO-RIGHT
