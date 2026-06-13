---
entity_id: "reaction.ecocyc.RXN-17751"
entity_type: "reaction"
name: "RXN-17751"
source_database: "EcoCyc"
source_id: "RXN-17751"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17751

`reaction.ecocyc.RXN-17751`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17751`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-OXOBUTANOATE + PROTON + E- -> CPD-3564; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-OXOBUTANOATE + PROTON + E- -> CPD-3564; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), 2-Oxobutanoate (molecule.C00109). Products: 2-Hydroxybutanoic acid (molecule.C05984).

## Annotation

2-OXOBUTANOATE + PROTON + E- -> CPD-3564; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C05984|molecule.C05984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17751`

## Notes

2-OXOBUTANOATE + PROTON + E- -> CPD-3564; direction=PHYSIOL-LEFT-TO-RIGHT
