---
entity_id: "reaction.ecocyc.TRANS-RXN-142"
entity_type: "reaction"
name: "indole:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-142"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# indole:proton symport

`reaction.ecocyc.TRANS-RXN-142`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-142`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + INDOLE -> PROTON + INDOLE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + INDOLE -> PROTON + INDOLE; direction=REVERSIBLE.

## Biological Role

Catalyzed by mtr (protein.P0AAD2). Substrates: H+ (molecule.C00080), Indole (molecule.C00463). Products: H+ (molecule.C00080), Indole (molecule.C00463).

## Annotation

PROTON + INDOLE -> PROTON + INDOLE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAD2|protein.P0AAD2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-142`

## Notes

PROTON + INDOLE -> PROTON + INDOLE; direction=REVERSIBLE
