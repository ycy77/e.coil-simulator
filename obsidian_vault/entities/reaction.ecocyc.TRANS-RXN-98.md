---
entity_id: "reaction.ecocyc.TRANS-RXN-98"
entity_type: "reaction"
name: "glucoronoside:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-98"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glucoronoside:proton symport

`reaction.ecocyc.TRANS-RXN-98`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-98`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + Glucuronides -> PROTON + Glucuronides; direction=REVERSIBLE EcoCyc reaction equation: PROTON + Glucuronides -> PROTON + Glucuronides; direction=REVERSIBLE.

## Biological Role

Catalyzed by uidB (protein.P0CE44). Substrates: H+ (molecule.C00080), a D-glucuronide (molecule.ecocyc.Glucuronides). Products: H+ (molecule.C00080), a D-glucuronide (molecule.ecocyc.Glucuronides).

## Annotation

PROTON + Glucuronides -> PROTON + Glucuronides; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0CE44|protein.P0CE44]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Glucuronides|molecule.ecocyc.Glucuronides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Glucuronides|molecule.ecocyc.Glucuronides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-98`

## Notes

PROTON + Glucuronides -> PROTON + Glucuronides; direction=REVERSIBLE
