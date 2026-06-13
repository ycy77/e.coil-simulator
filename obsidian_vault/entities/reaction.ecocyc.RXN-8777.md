---
entity_id: "reaction.ecocyc.RXN-8777"
entity_type: "reaction"
name: "RXN-8777"
source_database: "EcoCyc"
source_id: "RXN-8777"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8777

`reaction.ecocyc.RXN-8777`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8777`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-DH-3-DO-D-ARABINONATE -> CPD-654 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-DH-3-DO-D-ARABINONATE -> CPD-654 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: 2-Dehydro-3-deoxy-D-xylonate (molecule.C03826). Products: H2O (molecule.C00001), 2,5-Dioxopentanoate (molecule.C00433).

## Enriched Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Annotation

2-DH-3-DO-D-ARABINONATE -> CPD-654 + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6760` D-xylose degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00433|molecule.C00433]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03826|molecule.C03826]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8777`

## Notes

2-DH-3-DO-D-ARABINONATE -> CPD-654 + WATER; direction=LEFT-TO-RIGHT
