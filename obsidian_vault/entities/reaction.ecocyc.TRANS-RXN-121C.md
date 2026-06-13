---
entity_id: "reaction.ecocyc.TRANS-RXN-121C"
entity_type: "reaction"
name: "orotate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-121C"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# orotate:proton symport

`reaction.ecocyc.TRANS-RXN-121C`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-121C`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + OROTATE -> PROTON + OROTATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + OROTATE -> PROTON + OROTATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by dctA (protein.P0A830). Substrates: H+ (molecule.C00080), Orotate (molecule.C00295). Products: H+ (molecule.C00080), Orotate (molecule.C00295).

## Annotation

PROTON + OROTATE -> PROTON + OROTATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-121C`

## Notes

PROTON + OROTATE -> PROTON + OROTATE; direction=REVERSIBLE
