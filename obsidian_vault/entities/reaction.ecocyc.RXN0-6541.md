---
entity_id: "reaction.ecocyc.RXN0-6541"
entity_type: "reaction"
name: "RXN0-6541"
source_database: "EcoCyc"
source_id: "RXN0-6541"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6541

`reaction.ecocyc.RXN0-6541`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6541`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-SEDOHEPTULOSE-7-P + ATP -> PROTON + D-SEDOHEPTULOSE-1-7-P2 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-SEDOHEPTULOSE-7-P + ATP -> PROTON + D-SEDOHEPTULOSE-1-7-P2 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 6-phosphofructokinase 1 (complex.ecocyc.6PFK-1-CPX). Substrates: ATP (molecule.C00002), Sedoheptulose 7-phosphate (molecule.C05382). Products: ADP (molecule.C00008), H+ (molecule.C00080), Sedoheptulose 1,7-bisphosphate (molecule.C00447).

## Enriched Pathways

- `ecocyc.PWY0-1517` sedoheptulose bisphosphate bypass (EcoCyc)

## Annotation

D-SEDOHEPTULOSE-7-P + ATP -> PROTON + D-SEDOHEPTULOSE-1-7-P2 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1517` sedoheptulose bisphosphate bypass (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.6PFK-1-CPX|complex.ecocyc.6PFK-1-CPX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00447|molecule.C00447]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6541`

## Notes

D-SEDOHEPTULOSE-7-P + ATP -> PROTON + D-SEDOHEPTULOSE-1-7-P2 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
