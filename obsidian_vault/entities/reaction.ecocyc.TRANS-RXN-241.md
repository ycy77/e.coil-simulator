---
entity_id: "reaction.ecocyc.TRANS-RXN-241"
entity_type: "reaction"
name: "Mn2+:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-241"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Mn2+:proton symport

`reaction.ecocyc.TRANS-RXN-241`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-241`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MN+2 + PROTON -> MN+2 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: MN+2 + PROTON -> MN+2 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mntH (protein.P0A769). Substrates: H+ (molecule.C00080), Mn2+ (molecule.ecocyc.MN_2). Products: H+ (molecule.C00080), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

MN+2 + PROTON -> MN+2 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A769|protein.P0A769]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-241`

## Notes

MN+2 + PROTON -> MN+2 + PROTON; direction=REVERSIBLE
