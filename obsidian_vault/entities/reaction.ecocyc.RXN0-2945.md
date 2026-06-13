---
entity_id: "reaction.ecocyc.RXN0-2945"
entity_type: "reaction"
name: "RXN0-2945"
source_database: "EcoCyc"
source_id: "RXN0-2945"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2945

`reaction.ecocyc.RXN0-2945`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2945`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CU+ + PROTON + OXYGEN-MOLECULE -> CU+2 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CU+ + PROTON + OXYGEN-MOLECULE -> CU+2 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cueO (protein.P36649). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), Cu+ (molecule.ecocyc.CU_). Products: H2O (molecule.C00001), Cu2+ (molecule.ecocyc.CU_2).

## Annotation

CU+ + PROTON + OXYGEN-MOLECULE -> CU+2 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P36649|protein.P36649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2945`

## Notes

CU+ + PROTON + OXYGEN-MOLECULE -> CU+2 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
