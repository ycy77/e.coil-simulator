---
entity_id: "reaction.ecocyc.RXN-15952"
entity_type: "reaction"
name: "RXN-15952"
source_database: "EcoCyc"
source_id: "RXN-15952"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15952

`reaction.ecocyc.RXN-15952`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15952`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cyclic-Phosphate-Terminated-RNAs + WATER -> 2-Prime-Phosphate-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Cyclic-Phosphate-Terminated-RNAs + WATER -> 2-Prime-Phosphate-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by thpR (protein.P37025). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080).

## Annotation

Cyclic-Phosphate-Terminated-RNAs + WATER -> 2-Prime-Phosphate-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37025|protein.P37025]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15952`

## Notes

Cyclic-Phosphate-Terminated-RNAs + WATER -> 2-Prime-Phosphate-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
