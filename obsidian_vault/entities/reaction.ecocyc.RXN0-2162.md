---
entity_id: "reaction.ecocyc.RXN0-2162"
entity_type: "reaction"
name: "arginine:agmatine antiport"
source_database: "EcoCyc"
source_id: "RXN0-2162"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# arginine:agmatine antiport

`reaction.ecocyc.RXN0-2162`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2162`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

AGMATHINE + ARG -> AGMATHINE + ARG; direction=REVERSIBLE EcoCyc reaction equation: AGMATHINE + ARG -> AGMATHINE + ARG; direction=REVERSIBLE.

## Biological Role

Catalyzed by arginine:agmatine antiporter (complex.ecocyc.CPLX0-7535). Substrates: L-Arginine (molecule.C00062), Agmatine (molecule.C00179). Products: L-Arginine (molecule.C00062), Agmatine (molecule.C00179).

## Annotation

AGMATHINE + ARG -> AGMATHINE + ARG; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7535|complex.ecocyc.CPLX0-7535]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00179|molecule.C00179]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00179|molecule.C00179]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2162`

## Notes

AGMATHINE + ARG -> AGMATHINE + ARG; direction=REVERSIBLE
