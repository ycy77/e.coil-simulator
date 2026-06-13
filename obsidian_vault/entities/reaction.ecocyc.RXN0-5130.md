---
entity_id: "reaction.ecocyc.RXN0-5130"
entity_type: "reaction"
name: "D-serine:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-5130"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-serine:proton symport

`reaction.ecocyc.RXN0-5130`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5130`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + D-SERINE -> PROTON + D-SERINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + D-SERINE -> PROTON + D-SERINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by cycA (protein.P0AAE0). Substrates: H+ (molecule.C00080), D-Serine (molecule.C00740). Products: H+ (molecule.C00080), D-Serine (molecule.C00740).

## Annotation

PROTON + D-SERINE -> PROTON + D-SERINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5130`

## Notes

PROTON + D-SERINE -> PROTON + D-SERINE; direction=REVERSIBLE
