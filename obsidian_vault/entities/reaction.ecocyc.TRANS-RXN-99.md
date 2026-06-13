---
entity_id: "reaction.ecocyc.TRANS-RXN-99"
entity_type: "reaction"
name: "choline:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-99"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# choline:proton symport

`reaction.ecocyc.TRANS-RXN-99`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-99`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CHOLINE -> PROTON + CHOLINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CHOLINE -> PROTON + CHOLINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by betT (protein.P0ABC9). Substrates: H+ (molecule.C00080), Choline (molecule.C00114). Products: H+ (molecule.C00080), Choline (molecule.C00114).

## Annotation

PROTON + CHOLINE -> PROTON + CHOLINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABC9|protein.P0ABC9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-99`

## Notes

PROTON + CHOLINE -> PROTON + CHOLINE; direction=REVERSIBLE
