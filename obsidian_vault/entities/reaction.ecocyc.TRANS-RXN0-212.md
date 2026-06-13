---
entity_id: "reaction.ecocyc.TRANS-RXN0-212"
entity_type: "reaction"
name: "cadaverine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-212"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cadaverine:proton symport

`reaction.ecocyc.TRANS-RXN0-212`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-212`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CADAVERINE -> PROTON + CADAVERINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CADAVERINE -> PROTON + CADAVERINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by cadB (protein.P0AAE8). Substrates: H+ (molecule.C00080), Cadaverine (molecule.C01672). Products: H+ (molecule.C00080), Cadaverine (molecule.C01672).

## Annotation

PROTON + CADAVERINE -> PROTON + CADAVERINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE8|protein.P0AAE8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-212`

## Notes

PROTON + CADAVERINE -> PROTON + CADAVERINE; direction=REVERSIBLE
