---
entity_id: "reaction.ecocyc.RXN-11397"
entity_type: "reaction"
name: "RXN-11397"
source_database: "EcoCyc"
source_id: "RXN-11397"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11397

`reaction.ecocyc.RXN-11397`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11397`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12366 + WATER -> PROTON + CPD-12367 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12366 + WATER -> PROTON + CPD-12367 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutT (protein.P08337). Substrates: H2O (molecule.C00001), 8-oxo-GTP (molecule.ecocyc.CPD-12366). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), 8-oxo-GMP (molecule.ecocyc.CPD-12367).

## Annotation

CPD-12366 + WATER -> PROTON + CPD-12367 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08337|protein.P08337]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12367|molecule.ecocyc.CPD-12367]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12366|molecule.ecocyc.CPD-12366]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11397`

## Notes

CPD-12366 + WATER -> PROTON + CPD-12367 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
