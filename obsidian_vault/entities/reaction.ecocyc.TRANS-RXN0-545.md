---
entity_id: "reaction.ecocyc.TRANS-RXN0-545"
entity_type: "reaction"
name: "passive diffusion of CO2"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-545"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG|CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# passive diffusion of CO2

`reaction.ecocyc.TRANS-RXN0-545`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-545`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG|CCO-OUTER-MEM

## Enriched Summary

Pure phospholipid artificial membranes are permeable to gases, such as CO2, O2, N2 and NH3 . EcoCyc reaction equation: CARBON-DIOXIDE -> CARBON-DIOXIDE; direction=REVERSIBLE. Pure phospholipid artificial membranes are permeable to gases, such as CO2, O2, N2 and NH3 .

## Biological Role

Substrates: CO2 (molecule.C00011). Products: CO2 (molecule.C00011).

## Annotation

Pure phospholipid artificial membranes are permeable to gases, such as CO2, O2, N2 and NH3 .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-545`

## Notes

CARBON-DIOXIDE -> CARBON-DIOXIDE; direction=REVERSIBLE
