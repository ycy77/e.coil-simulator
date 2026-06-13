---
entity_id: "reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN"
entity_type: "reaction"
name: "THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN

`reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S2O3 + GLUTATHIONE -> PROTON + SO3 + HS + OXIDIZED-GLUTATHIONE; direction= EcoCyc reaction equation: S2O3 + GLUTATHIONE -> PROTON + SO3 + HS + OXIDIZED-GLUTATHIONE; direction=.

## Biological Role

Substrates: Glutathione (molecule.C00051), Thiosulfate (molecule.C00320). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), Glutathione disulfide (molecule.C00127), Hydrogen sulfide (molecule.C00283).

## Annotation

S2O3 + GLUTATHIONE -> PROTON + SO3 + HS + OXIDIZED-GLUTATHIONE; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN`

## Notes

S2O3 + GLUTATHIONE -> PROTON + SO3 + HS + OXIDIZED-GLUTATHIONE; direction=
