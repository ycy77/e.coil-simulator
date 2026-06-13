---
entity_id: "reaction.ecocyc.RXN-22319"
entity_type: "reaction"
name: "RXN-22319"
source_database: "EcoCyc"
source_id: "RXN-22319"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22319

`reaction.ecocyc.RXN-22319`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22319`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-24335 -> ACET + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-24335 -> ACET + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: Acetate (molecule.C00033). Products: Acetate (molecule.C00033), H+ (molecule.C00080).

## Annotation

CPD-24335 -> ACET + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22319`

## Notes

CPD-24335 -> ACET + PROTON; direction=REVERSIBLE
