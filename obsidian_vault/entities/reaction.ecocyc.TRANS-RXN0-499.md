---
entity_id: "reaction.ecocyc.TRANS-RXN0-499"
entity_type: "reaction"
name: "succinate:tartrate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-499"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# succinate:tartrate antiport

`reaction.ecocyc.TRANS-RXN0-499`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-499`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-TARTRATE + SUC -> SUC + D-TARTRATE; direction=REVERSIBLE EcoCyc reaction equation: D-TARTRATE + SUC -> SUC + D-TARTRATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuB (protein.P0ABN9). Substrates: Succinate (molecule.C00042), D-tartrate (molecule.ecocyc.D-TARTRATE). Products: Succinate (molecule.C00042), D-tartrate (molecule.ecocyc.D-TARTRATE).

## Annotation

D-TARTRATE + SUC -> SUC + D-TARTRATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABN9|protein.P0ABN9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-TARTRATE|molecule.ecocyc.D-TARTRATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-TARTRATE|molecule.ecocyc.D-TARTRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-499`

## Notes

D-TARTRATE + SUC -> SUC + D-TARTRATE; direction=REVERSIBLE
