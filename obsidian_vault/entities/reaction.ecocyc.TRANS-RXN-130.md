---
entity_id: "reaction.ecocyc.TRANS-RXN-130"
entity_type: "reaction"
name: "Na+:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-130"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Na+:proton antiport

`reaction.ecocyc.TRANS-RXN-130`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-130`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + NA+ -> NA+ + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PROTON + NA+ -> NA+ + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by nhaB (protein.P0AFA7). Substrates: H+ (molecule.C00080), Sodium cation (molecule.C01330). Products: H+ (molecule.C00080), Sodium cation (molecule.C01330).

## Annotation

PROTON + NA+ -> NA+ + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AFA7|protein.P0AFA7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-10324|molecule.ecocyc.CPD-10324]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9939|molecule.ecocyc.CPD-9939]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-130`

## Notes

PROTON + NA+ -> NA+ + PROTON; direction=REVERSIBLE
