---
entity_id: "reaction.ecocyc.TRANS-RXN-77"
entity_type: "reaction"
name: "L-tyrosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-77"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-tyrosine:proton symport

`reaction.ecocyc.TRANS-RXN-77`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-77`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + TYR -> PROTON + TYR; direction=REVERSIBLE EcoCyc reaction equation: PROTON + TYR -> PROTON + TYR; direction=REVERSIBLE.

## Biological Role

Catalyzed by tyrP (protein.P0AAD4), aroP (protein.P15993). Substrates: H+ (molecule.C00080), L-Tyrosine (molecule.C00082). Products: H+ (molecule.C00080), L-Tyrosine (molecule.C00082).

## Annotation

PROTON + TYR -> PROTON + TYR; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AAD4|protein.P0AAD4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P15993|protein.P15993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-77`

## Notes

PROTON + TYR -> PROTON + TYR; direction=REVERSIBLE
