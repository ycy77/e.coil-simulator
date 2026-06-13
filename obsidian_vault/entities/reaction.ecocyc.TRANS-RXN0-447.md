---
entity_id: "reaction.ecocyc.TRANS-RXN0-447"
entity_type: "reaction"
name: "adenine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-447"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# adenine:proton symport

`reaction.ecocyc.TRANS-RXN0-447`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-447`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ADENINE + PROTON -> ADENINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: ADENINE + PROTON -> ADENINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by adeP (protein.P31466). Substrates: H+ (molecule.C00080), Adenine (molecule.C00147). Products: H+ (molecule.C00080), Adenine (molecule.C00147).

## Annotation

ADENINE + PROTON -> ADENINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P31466|protein.P31466]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-16183|molecule.ecocyc.CPD-16183]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2060|molecule.ecocyc.CPD0-2060]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-447`

## Notes

ADENINE + PROTON -> ADENINE + PROTON; direction=REVERSIBLE
