---
entity_id: "reaction.ecocyc.RXN0-2943"
entity_type: "reaction"
name: "RXN0-2943"
source_database: "EcoCyc"
source_id: "RXN0-2943"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2943

`reaction.ecocyc.RXN0-2943`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2943`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

2-3-DIHYDROXYBENZOATE + OXYGEN-MOLECULE -> PROTON + 2-CARBOXYMUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-3-DIHYDROXYBENZOATE + OXYGEN-MOLECULE -> PROTON + 2-CARBOXYMUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cueO (protein.P36649). Substrates: Oxygen (molecule.C00007), 2,3-Dihydroxybenzoate (molecule.C00196). Products: H+ (molecule.C00080), 2-carboxymuconate (molecule.ecocyc.2-CARBOXYMUCONATE).

## Annotation

2-3-DIHYDROXYBENZOATE + OXYGEN-MOLECULE -> PROTON + 2-CARBOXYMUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P36649|protein.P36649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-CARBOXYMUCONATE|molecule.ecocyc.2-CARBOXYMUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00196|molecule.C00196]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2943`

## Notes

2-3-DIHYDROXYBENZOATE + OXYGEN-MOLECULE -> PROTON + 2-CARBOXYMUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT
