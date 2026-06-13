---
entity_id: "reaction.ecocyc.RXN-19629"
entity_type: "reaction"
name: "RXN-19629"
source_database: "EcoCyc"
source_id: "RXN-19629"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19629

`reaction.ecocyc.RXN-19629`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19629`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTATHIONE + SULFO-CYSTEINE -> OXIDIZED-GLUTATHIONE + CYS + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + SULFO-CYSTEINE -> OXIDIZED-GLUTATHIONE + CYS + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by grxA (protein.P68688). Substrates: Glutathione (molecule.C00051), S-Sulfo-L-cysteine (molecule.C05824). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), L-Cysteine (molecule.C00097), Glutathione disulfide (molecule.C00127).

## Annotation

GLUTATHIONE + SULFO-CYSTEINE -> OXIDIZED-GLUTATHIONE + CYS + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P68688|protein.P68688]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05824|molecule.C05824]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19629`

## Notes

GLUTATHIONE + SULFO-CYSTEINE -> OXIDIZED-GLUTATHIONE + CYS + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
