---
entity_id: "reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN"
entity_type: "reaction"
name: "GLUTATHIONE-PEROXIDASE-RXN"
source_database: "EcoCyc"
source_id: "GLUTATHIONE-PEROXIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTATHIONE-PEROXIDASE-RXN

`reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTATHIONE-PEROXIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROGEN-PEROXIDE + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: HYDROGEN-PEROXIDE + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by btuE (protein.P06610). Substrates: Hydrogen peroxide (molecule.C00027), Glutathione (molecule.C00051). Products: H2O (molecule.C00001), Glutathione disulfide (molecule.C00127).

## Annotation

HYDROGEN-PEROXIDE + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P06610|protein.P06610]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUTATHIONE-PEROXIDASE-RXN`

## Notes

HYDROGEN-PEROXIDE + GLUTATHIONE -> OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT
