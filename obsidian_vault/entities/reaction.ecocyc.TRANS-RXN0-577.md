---
entity_id: "reaction.ecocyc.TRANS-RXN0-577"
entity_type: "reaction"
name: "transport of adenine"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-577"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# transport of adenine

`reaction.ecocyc.TRANS-RXN0-577`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-577`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ADENINE -> ADENINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ADENINE -> ADENINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by adeQ (protein.P31440). Substrates: Adenine (molecule.C00147). Products: Adenine (molecule.C00147).

## Annotation

ADENINE -> ADENINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P31440|protein.P31440]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-16183|molecule.ecocyc.CPD-16183]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2060|molecule.ecocyc.CPD0-2060]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-577`

## Notes

ADENINE -> ADENINE; direction=LEFT-TO-RIGHT
