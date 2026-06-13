---
entity_id: "reaction.ecocyc.RXN0-5203"
entity_type: "reaction"
name: "D-cycloserine:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-5203"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-cycloserine:proton symport

`reaction.ecocyc.RXN0-5203`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5203`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-2482 -> PROTON + CPD-2482; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD-2482 -> PROTON + CPD-2482; direction=REVERSIBLE.

## Biological Role

Catalyzed by cycA (protein.P0AAE0). Substrates: H+ (molecule.C00080), D-cycloserine (molecule.ecocyc.CPD-2482). Products: H+ (molecule.C00080), D-cycloserine (molecule.ecocyc.CPD-2482).

## Annotation

PROTON + CPD-2482 -> PROTON + CPD-2482; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-2482|molecule.ecocyc.CPD-2482]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-2482|molecule.ecocyc.CPD-2482]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5203`

## Notes

PROTON + CPD-2482 -> PROTON + CPD-2482; direction=REVERSIBLE
