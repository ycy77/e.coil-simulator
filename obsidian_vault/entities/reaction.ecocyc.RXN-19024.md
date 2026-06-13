---
entity_id: "reaction.ecocyc.RXN-19024"
entity_type: "reaction"
name: "RXN-19024"
source_database: "EcoCyc"
source_id: "RXN-19024"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19024

`reaction.ecocyc.RXN-19024`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19024`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTATHIONE -> CYS-GLY + 5-OXOPROLINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE -> CYS-GLY + 5-OXOPROLINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by chaC (protein.P39163). Substrates: Glutathione (molecule.C00051). Products: Cys-Gly (molecule.C01419), 5-Oxoproline (molecule.C01879).

## Annotation

GLUTATHIONE -> CYS-GLY + 5-OXOPROLINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P39163|protein.P39163]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01419|molecule.C01419]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01879|molecule.C01879]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19024`

## Notes

GLUTATHIONE -> CYS-GLY + 5-OXOPROLINE; direction=PHYSIOL-LEFT-TO-RIGHT
