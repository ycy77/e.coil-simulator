---
entity_id: "reaction.ecocyc.RXN-20410"
entity_type: "reaction"
name: "RXN-20410"
source_database: "EcoCyc"
source_id: "RXN-20410"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20410

`reaction.ecocyc.RXN-20410`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20410`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-containing-abasic-Sites + WATER -> a-5-deoxyribose-5-phosphate-DNA + 3-Hydroxy-Terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-containing-abasic-Sites + WATER -> a-5-deoxyribose-5-phosphate-DNA + 3-Hydroxy-Terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by xthA (protein.P09030), nfo (protein.P0A6C1). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080).

## Annotation

DNA-containing-abasic-Sites + WATER -> a-5-deoxyribose-5-phosphate-DNA + 3-Hydroxy-Terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P09030|protein.P09030]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A6C1|protein.P0A6C1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20410`

## Notes

DNA-containing-abasic-Sites + WATER -> a-5-deoxyribose-5-phosphate-DNA + 3-Hydroxy-Terminated-DNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
