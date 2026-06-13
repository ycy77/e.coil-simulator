---
entity_id: "reaction.ecocyc.CDPDIGLYSYN-RXN"
entity_type: "reaction"
name: "CDPDIGLYSYN-RXN"
source_database: "EcoCyc"
source_id: "CDPDIGLYSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CDPDIGLYSYN-RXN

`reaction.ecocyc.CDPDIGLYSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CDPDIGLYSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the phospholipid biosynthesis pathway. EcoCyc reaction equation: CTP + L-PHOSPHATIDATE + PROTON -> PPI + CDPDIACYLGLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the phospholipid biosynthesis pathway.

## Biological Role

Catalyzed by cdsA (protein.P0ABG1). Substrates: CTP (molecule.C00063), H+ (molecule.C00080), Phosphatidate (molecule.C00416). Products: Diphosphate (molecule.C00013), CDP-diacylglycerol (molecule.C00269).

## Enriched Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Annotation

This reaction is part of the phospholipid biosynthesis pathway.

## Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ABG1|protein.P0ABG1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00269|molecule.C00269]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CDPDIGLYSYN-RXN`

## Notes

CTP + L-PHOSPHATIDATE + PROTON -> PPI + CDPDIACYLGLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT
