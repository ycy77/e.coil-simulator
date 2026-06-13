---
entity_id: "reaction.ecocyc.RXN-12864"
entity_type: "reaction"
name: "Painter reaction"
source_database: "EcoCyc"
source_id: "RXN-12864"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Painter reaction

`reaction.ecocyc.RXN-12864`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12864`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SELENITE + GLUTATHIONE + PROTON -> CPD-13908 + OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: SELENITE + GLUTATHIONE + PROTON -> CPD-13908 + OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), H+ (molecule.C00080), Selenite (molecule.C05684). Products: H2O (molecule.C00001), Glutathione disulfide (molecule.C00127), Selenodiglutathione (molecule.C18870).

## Annotation

SELENITE + GLUTATHIONE + PROTON -> CPD-13908 + OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C18870|molecule.C18870]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05684|molecule.C05684]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12864`

## Notes

SELENITE + GLUTATHIONE + PROTON -> CPD-13908 + OXIDIZED-GLUTATHIONE + WATER; direction=LEFT-TO-RIGHT
