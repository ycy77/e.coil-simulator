---
entity_id: "reaction.ecocyc.RXN-22315"
entity_type: "reaction"
name: "RXN-22315"
source_database: "EcoCyc"
source_id: "RXN-22315"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22315

`reaction.ecocyc.RXN-22315`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22315`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2040 -> CPD-763 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2040 -> CPD-763 + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: arsenous acid (molecule.ecocyc.CPD0-2040). Products: H+ (molecule.C00080), arsenite (molecule.ecocyc.CPD-763).

## Annotation

CPD0-2040 -> CPD-763 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22315`

## Notes

CPD0-2040 -> CPD-763 + PROTON; direction=REVERSIBLE
