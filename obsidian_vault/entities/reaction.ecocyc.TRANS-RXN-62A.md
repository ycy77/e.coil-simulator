---
entity_id: "reaction.ecocyc.TRANS-RXN-62A"
entity_type: "reaction"
name: "D-alanine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-62A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-alanine:proton symport

`reaction.ecocyc.TRANS-RXN-62A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-62A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + D-ALANINE -> PROTON + D-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + D-ALANINE -> PROTON + D-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by cycA (protein.P0AAE0). Substrates: H+ (molecule.C00080), D-Alanine (molecule.C00133). Products: H+ (molecule.C00080), D-Alanine (molecule.C00133).

## Annotation

PROTON + D-ALANINE -> PROTON + D-ALANINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-62A`

## Notes

PROTON + D-ALANINE -> PROTON + D-ALANINE; direction=REVERSIBLE
