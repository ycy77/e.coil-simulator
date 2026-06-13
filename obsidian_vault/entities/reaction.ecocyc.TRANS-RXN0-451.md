---
entity_id: "reaction.ecocyc.TRANS-RXN0-451"
entity_type: "reaction"
name: "malate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-451"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# malate:proton symport

`reaction.ecocyc.TRANS-RXN0-451`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-451`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-660 + PROTON -> CPD-660 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-660 + PROTON -> CPD-660 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by dctA (protein.P0A830). Substrates: H+ (molecule.C00080), (R)-Malate (molecule.C00497). Products: H+ (molecule.C00080), (R)-Malate (molecule.C00497).

## Annotation

CPD-660 + PROTON -> CPD-660 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-451`

## Notes

CPD-660 + PROTON -> CPD-660 + PROTON; direction=REVERSIBLE
