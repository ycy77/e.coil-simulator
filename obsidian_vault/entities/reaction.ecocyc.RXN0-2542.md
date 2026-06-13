---
entity_id: "reaction.ecocyc.RXN0-2542"
entity_type: "reaction"
name: "RXN0-2542"
source_database: "EcoCyc"
source_id: "RXN0-2542"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2542

`reaction.ecocyc.RXN0-2542`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2542`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

CPD-18254 -> CPD-18254; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18254 -> CPD-18254; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ompG (protein.P76045). Substrates: hydrophilic solute < 900 Da (molecule.ecocyc.CPD-18254). Products: hydrophilic solute < 900 Da (molecule.ecocyc.CPD-18254).

## Annotation

CPD-18254 -> CPD-18254; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76045|protein.P76045]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18254|molecule.ecocyc.CPD-18254]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18254|molecule.ecocyc.CPD-18254]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2542`

## Notes

CPD-18254 -> CPD-18254; direction=LEFT-TO-RIGHT
