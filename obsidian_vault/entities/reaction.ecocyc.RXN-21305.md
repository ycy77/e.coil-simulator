---
entity_id: "reaction.ecocyc.RXN-21305"
entity_type: "reaction"
name: "RXN-21305"
source_database: "EcoCyc"
source_id: "RXN-21305"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21305

`reaction.ecocyc.RXN-21305`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21305`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-DNA-3-deoxyribose-5-phosphate + WATER -> 3-Hydroxy-Terminated-DNAs + DEOXY-RIBOSE-5P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-DNA-3-deoxyribose-5-phosphate + WATER -> 3-Hydroxy-Terminated-DNAs + DEOXY-RIBOSE-5P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nfo (protein.P0A6C1). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), 2-Deoxy-D-ribose 5-phosphate (molecule.C00673).

## Annotation

a-DNA-3-deoxyribose-5-phosphate + WATER -> 3-Hydroxy-Terminated-DNAs + DEOXY-RIBOSE-5P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A6C1|protein.P0A6C1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00673|molecule.C00673]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21305`

## Notes

a-DNA-3-deoxyribose-5-phosphate + WATER -> 3-Hydroxy-Terminated-DNAs + DEOXY-RIBOSE-5P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
