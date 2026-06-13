---
entity_id: "reaction.ecocyc.RXN-1623"
entity_type: "reaction"
name: "RXN-1623"
source_database: "EcoCyc"
source_id: "RXN-1623"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-1623

`reaction.ecocyc.RXN-1623`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-1623`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACYL-COA + ACYL-SN-GLYCEROL-3P -> CO-A + L-PHOSPHATIDATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ACYL-COA + ACYL-SN-GLYCEROL-3P -> CO-A + L-PHOSPHATIDATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsC (protein.P26647), yihG (protein.P32129). Substrates: Acyl-CoA (molecule.C00040), 1-Acyl-sn-glycerol 3-phosphate (molecule.C00681). Products: CoA (molecule.C00010), Phosphatidate (molecule.C00416).

## Enriched Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)

## Annotation

ACYL-COA + ACYL-SN-GLYCEROL-3P -> CO-A + L-PHOSPHATIDATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P32129|protein.P32129]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00040|molecule.C00040]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00681|molecule.C00681]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-1623`

## Notes

ACYL-COA + ACYL-SN-GLYCEROL-3P -> CO-A + L-PHOSPHATIDATE; direction=LEFT-TO-RIGHT
