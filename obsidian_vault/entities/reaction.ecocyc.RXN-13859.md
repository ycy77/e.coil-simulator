---
entity_id: "reaction.ecocyc.RXN-13859"
entity_type: "reaction"
name: "RXN-13859"
source_database: "EcoCyc"
source_id: "RXN-13859"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13859

`reaction.ecocyc.RXN-13859`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13859`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + NIACINAMIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NAD + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + NIACINAMIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADNUCLEOSID-MONOMER (protein.ecocyc.NADNUCLEOSID-MONOMER). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003). Products: H+ (molecule.C00080), Nicotinamide (molecule.C00153), ADP-ribose (molecule.C00301).

## Annotation

NAD + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + NIACINAMIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.ecocyc.NADNUCLEOSID-MONOMER|protein.ecocyc.NADNUCLEOSID-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00301|molecule.C00301]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13859`

## Notes

NAD + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + NIACINAMIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
