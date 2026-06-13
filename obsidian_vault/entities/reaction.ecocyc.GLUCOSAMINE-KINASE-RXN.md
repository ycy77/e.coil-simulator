---
entity_id: "reaction.ecocyc.GLUCOSAMINE-KINASE-RXN"
entity_type: "reaction"
name: "GLUCOSAMINE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "GLUCOSAMINE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCOSAMINE-KINASE-RXN

`reaction.ecocyc.GLUCOSAMINE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCOSAMINE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUCOSAMINE + ATP -> D-GLUCOSAMINE-6-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUCOSAMINE + ATP -> D-GLUCOSAMINE-6-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glk (protein.P0A6V8). Substrates: ATP (molecule.C00002), D-Glucosamine (molecule.C00329). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Glucosamine 6-phosphate (molecule.C00352).

## Annotation

GLUCOSAMINE + ATP -> D-GLUCOSAMINE-6-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6V8|protein.P0A6V8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00329|molecule.C00329]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUCOSAMINE-KINASE-RXN`

## Notes

GLUCOSAMINE + ATP -> D-GLUCOSAMINE-6-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
