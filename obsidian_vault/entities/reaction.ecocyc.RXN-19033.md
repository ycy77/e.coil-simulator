---
entity_id: "reaction.ecocyc.RXN-19033"
entity_type: "reaction"
name: "RXN-19033"
source_database: "EcoCyc"
source_id: "RXN-19033"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19033

`reaction.ecocyc.RXN-19033`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19033`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTATHIONE + S2O3 -> CPD-11281 + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + S2O3 -> CPD-11281 + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pspE (protein.P23857). Substrates: Glutathione (molecule.C00051), Thiosulfate (molecule.C00320). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), S-Sulfanylglutathione (molecule.C17267).

## Annotation

GLUTATHIONE + S2O3 -> CPD-11281 + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P23857|protein.P23857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C17267|molecule.C17267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19033`

## Notes

GLUTATHIONE + S2O3 -> CPD-11281 + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
