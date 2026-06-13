---
entity_id: "reaction.ecocyc.PRODISULFREDUCT-RXN"
entity_type: "reaction"
name: "PRODISULFREDUCT-RXN"
source_database: "EcoCyc"
source_id: "PRODISULFREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PRODISULFREDUCT-RXN

`reaction.ecocyc.PRODISULFREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRODISULFREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTATHIONE + Protein-Ox-Disulfides -> OXIDIZED-GLUTATHIONE + Protein-Red-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + Protein-Ox-Disulfides -> OXIDIZED-GLUTATHIONE + Protein-Red-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by grxB (protein.P0AC59), grxC (protein.P0AC62), grxA (protein.P68688). Substrates: Glutathione (molecule.C00051). Products: Glutathione disulfide (molecule.C00127).

## Annotation

GLUTATHIONE + Protein-Ox-Disulfides -> OXIDIZED-GLUTATHIONE + Protein-Red-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AC59|protein.P0AC59]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AC62|protein.P0AC62]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P68688|protein.P68688]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PRODISULFREDUCT-RXN`

## Notes

GLUTATHIONE + Protein-Ox-Disulfides -> OXIDIZED-GLUTATHIONE + Protein-Red-Disulfides; direction=PHYSIOL-LEFT-TO-RIGHT
