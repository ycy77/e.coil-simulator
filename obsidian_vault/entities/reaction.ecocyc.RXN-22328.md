---
entity_id: "reaction.ecocyc.RXN-22328"
entity_type: "reaction"
name: "RXN-22328"
source_database: "EcoCyc"
source_id: "RXN-22328"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22328

`reaction.ecocyc.RXN-22328`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22328`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2039 -> ANTIMONITE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2039 -> ANTIMONITE + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: antimonous acid (molecule.ecocyc.CPD0-2039). Products: H+ (molecule.C00080), antimonite (molecule.ecocyc.ANTIMONITE).

## Annotation

CPD0-2039 -> ANTIMONITE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ANTIMONITE|molecule.ecocyc.ANTIMONITE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22328`

## Notes

CPD0-2039 -> ANTIMONITE + PROTON; direction=REVERSIBLE
