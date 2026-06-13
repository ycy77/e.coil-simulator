---
entity_id: "reaction.ecocyc.RXN-15297"
entity_type: "reaction"
name: "RXN-15297"
source_database: "EcoCyc"
source_id: "RXN-15297"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15297

`reaction.ecocyc.RXN-15297`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15297`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16501 + ATP -> CPD-16502 + ADP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-16501 + ATP -> CPD-16502 + ADP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yihV (protein.P32143). Substrates: ATP (molecule.C00002), 6-Deoxy-6-sulfo-D-fructose (molecule.C20830). Products: ADP (molecule.C00008), H+ (molecule.C00080), 6-Deoxy-6-sulfo-D-fructose 1-phosphate (molecule.C20831).

## Enriched Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Annotation

CPD-16501 + ATP -> CPD-16502 + ADP + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32143|protein.P32143]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20831|molecule.C20831]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20830|molecule.C20830]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15297`

## Notes

CPD-16501 + ATP -> CPD-16502 + ADP + PROTON; direction=LEFT-TO-RIGHT
