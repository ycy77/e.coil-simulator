---
entity_id: "reaction.ecocyc.RXN-17916"
entity_type: "reaction"
name: "RXN-17916"
source_database: "EcoCyc"
source_id: "RXN-17916"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17916

`reaction.ecocyc.RXN-17916`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17916`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 5-Phospho-RNA + PROTON -> A-5-prime-PP-5-prime-RNA + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + 5-Phospho-RNA + PROTON -> A-5-prime-PP-5-prime-RNA + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rtcA (protein.P46849). Substrates: ATP (molecule.C00002), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013).

## Annotation

ATP + 5-Phospho-RNA + PROTON -> A-5-prime-PP-5-prime-RNA + PPI; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P46849|protein.P46849]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17916`

## Notes

ATP + 5-Phospho-RNA + PROTON -> A-5-prime-PP-5-prime-RNA + PPI; direction=LEFT-TO-RIGHT
