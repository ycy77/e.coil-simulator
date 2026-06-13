---
entity_id: "reaction.ecocyc.TRANS-RXN0-533"
entity_type: "reaction"
name: "choline:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-533"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# choline:proton antiport

`reaction.ecocyc.TRANS-RXN0-533`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-533`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CHOLINE + PROTON -> CHOLINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CHOLINE + PROTON -> CHOLINE + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Choline (molecule.C00114). Products: H+ (molecule.C00080), Choline (molecule.C00114).

## Annotation

CHOLINE + PROTON -> CHOLINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-533`

## Notes

CHOLINE + PROTON -> CHOLINE + PROTON; direction=REVERSIBLE
