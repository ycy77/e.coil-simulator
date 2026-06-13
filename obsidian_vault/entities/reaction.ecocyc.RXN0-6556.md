---
entity_id: "reaction.ecocyc.RXN0-6556"
entity_type: "reaction"
name: "RXN0-6556"
source_database: "EcoCyc"
source_id: "RXN0-6556"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6556

`reaction.ecocyc.RXN0-6556`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6556`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Phospho-DNA + ATP + PROTON -> A-5-prime-PP-5-prime-DNA + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 5-Phospho-DNA + ATP + PROTON -> A-5-prime-PP-5-prime-DNA + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rtcA (protein.P46849). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), a 5'-phospho-[DNA] (molecule.ecocyc.5-Phospho-DNA). Products: Diphosphate (molecule.C00013).

## Annotation

5-Phospho-DNA + ATP + PROTON -> A-5-prime-PP-5-prime-DNA + PPI; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P46849|protein.P46849]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-Phospho-DNA|molecule.ecocyc.5-Phospho-DNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6556`

## Notes

5-Phospho-DNA + ATP + PROTON -> A-5-prime-PP-5-prime-DNA + PPI; direction=LEFT-TO-RIGHT
