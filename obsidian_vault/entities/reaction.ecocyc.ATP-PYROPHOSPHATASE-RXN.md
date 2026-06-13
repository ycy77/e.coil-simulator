---
entity_id: "reaction.ecocyc.ATP-PYROPHOSPHATASE-RXN"
entity_type: "reaction"
name: "ATP-PYROPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "ATP-PYROPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ATP-PYROPHOSPHATASE-RXN

`reaction.ecocyc.ATP-PYROPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ATP-PYROPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + ATP -> PROTON + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + ATP -> PROTON + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ycaO (protein.P75838). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

WATER + ATP -> PROTON + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75838|protein.P75838]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ATP-PYROPHOSPHATASE-RXN`

## Notes

WATER + ATP -> PROTON + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
