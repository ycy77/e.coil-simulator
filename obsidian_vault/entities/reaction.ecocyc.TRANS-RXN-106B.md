---
entity_id: "reaction.ecocyc.TRANS-RXN-106B"
entity_type: "reaction"
name: "malate:succinate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-106B"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# malate:succinate antiport

`reaction.ecocyc.TRANS-RXN-106B`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-106B`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

SUC + MAL -> MAL + SUC; direction=REVERSIBLE EcoCyc reaction equation: SUC + MAL -> MAL + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuA (protein.P0ABN5), dcuB (protein.P0ABN9). Substrates: Succinate (molecule.C00042), (S)-Malate (molecule.C00149). Products: Succinate (molecule.C00042), (S)-Malate (molecule.C00149).

## Annotation

SUC + MAL -> MAL + SUC; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABN9|protein.P0ABN9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-106B`

## Notes

SUC + MAL -> MAL + SUC; direction=REVERSIBLE
