---
entity_id: "reaction.ecocyc.TRANS-RXN0-571"
entity_type: "reaction"
name: "acetate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-571"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# acetate:proton symport

`reaction.ecocyc.TRANS-RXN0-571`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-571`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ACET + PROTON -> ACET + PROTON; direction=REVERSIBLE EcoCyc reaction equation: ACET + PROTON -> ACET + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by satP (protein.P0AC98). Substrates: Acetate (molecule.C00033), H+ (molecule.C00080). Products: Acetate (molecule.C00033), H+ (molecule.C00080).

## Annotation

ACET + PROTON -> ACET + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AC98|protein.P0AC98]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00180|molecule.C00180]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00246|molecule.C00246]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-571`

## Notes

ACET + PROTON -> ACET + PROTON; direction=REVERSIBLE
