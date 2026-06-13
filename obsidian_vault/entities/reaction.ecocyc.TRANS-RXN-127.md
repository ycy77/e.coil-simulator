---
entity_id: "reaction.ecocyc.TRANS-RXN-127"
entity_type: "reaction"
name: "L-tartrate:succinate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-127"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-tartrate:succinate antiport

`reaction.ecocyc.TRANS-RXN-127`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-127`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

TARTRATE + SUC -> TARTRATE + SUC; direction=REVERSIBLE EcoCyc reaction equation: TARTRATE + SUC -> TARTRATE + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by ttdT (protein.P39414). Substrates: Succinate (molecule.C00042), (R,R)-Tartaric acid (molecule.C00898). Products: Succinate (molecule.C00042), (R,R)-Tartaric acid (molecule.C00898).

## Annotation

TARTRATE + SUC -> TARTRATE + SUC; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39414|protein.P39414]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00898|molecule.C00898]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-127`

## Notes

TARTRATE + SUC -> TARTRATE + SUC; direction=REVERSIBLE
