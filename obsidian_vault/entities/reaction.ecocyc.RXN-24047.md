---
entity_id: "reaction.ecocyc.RXN-24047"
entity_type: "reaction"
name: "RXN-24047"
source_database: "EcoCyc"
source_id: "RXN-24047"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24047

`reaction.ecocyc.RXN-24047`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24047`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-prime-FAD-capped-RNA + WATER -> 5-Phospho-RNA + FAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-prime-FAD-capped-RNA + WATER -> 5-Phospho-RNA + FAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rnm (protein.P77766). Substrates: H2O (molecule.C00001). Products: FAD (molecule.C00016), H+ (molecule.C00080).

## Annotation

5-prime-FAD-capped-RNA + WATER -> 5-Phospho-RNA + FAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77766|protein.P77766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24047`

## Notes

5-prime-FAD-capped-RNA + WATER -> 5-Phospho-RNA + FAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
