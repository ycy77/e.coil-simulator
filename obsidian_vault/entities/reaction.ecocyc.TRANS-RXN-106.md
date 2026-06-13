---
entity_id: "reaction.ecocyc.TRANS-RXN-106"
entity_type: "reaction"
name: "fumarate:succinate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-106"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# fumarate:succinate antiport

`reaction.ecocyc.TRANS-RXN-106`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-106`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

SUC + FUM -> FUM + SUC; direction=REVERSIBLE EcoCyc reaction equation: SUC + FUM -> FUM + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuA (protein.P0ABN5), dcuB (protein.P0ABN9), dcuC (protein.P0ABP3). Substrates: Succinate (molecule.C00042), Fumarate (molecule.C00122). Products: Succinate (molecule.C00042), Fumarate (molecule.C00122).

## Annotation

SUC + FUM -> FUM + SUC; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABN9|protein.P0ABN9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABP3|protein.P0ABP3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-106`

## Notes

SUC + FUM -> FUM + SUC; direction=REVERSIBLE
