---
entity_id: "reaction.ecocyc.DEHYDDEOXGALACTKIN-RXN"
entity_type: "reaction"
name: "DEHYDDEOXGALACTKIN-RXN"
source_database: "EcoCyc"
source_id: "DEHYDDEOXGALACTKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEHYDDEOXGALACTKIN-RXN

`reaction.ecocyc.DEHYDDEOXGALACTKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEHYDDEOXGALACTKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step of galactonate catabolism. EcoCyc reaction equation: 2-DEHYDRO-3-DEOXY-D-GALACTONATE + ATP -> PROTON + DEHYDRO-DEOXY-GALACTONATE-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT. The second step of galactonate catabolism.

## Biological Role

Catalyzed by dgoK (protein.P31459). Substrates: ATP (molecule.C00002), 2-Dehydro-3-deoxy-D-galactonate (molecule.C01216). Products: ADP (molecule.C00008), H+ (molecule.C00080), 2-Dehydro-3-deoxy-6-phospho-D-galactonate (molecule.C01286).

## Enriched Pathways

- `ecocyc.GALACTCAT-PWY` D-galactonate degradation (EcoCyc)

## Annotation

The second step of galactonate catabolism.

## Pathways

- `ecocyc.GALACTCAT-PWY` D-galactonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P31459|protein.P31459]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01286|molecule.C01286]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01216|molecule.C01216]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEHYDDEOXGALACTKIN-RXN`

## Notes

2-DEHYDRO-3-DEOXY-D-GALACTONATE + ATP -> PROTON + DEHYDRO-DEOXY-GALACTONATE-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT
