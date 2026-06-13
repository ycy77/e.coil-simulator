---
entity_id: "reaction.ecocyc.KDUD-RXN"
entity_type: "reaction"
name: "KDUD-RXN"
source_database: "EcoCyc"
source_id: "KDUD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDUD-RXN

`reaction.ecocyc.KDUD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDUD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + DE-O-GLUCONATE -> PROTON + NADH + DE-O-K-GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NAD + DE-O-GLUCONATE -> PROTON + NADH + DE-O-K-GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), 2-deoxy-D-gluconate (molecule.ecocyc.DE-O-GLUCONATE). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-dehydro-2-deoxy-D-gluconate (molecule.ecocyc.DE-O-K-GLUCONATE).

## Annotation

NAD + DE-O-GLUCONATE -> PROTON + NADH + DE-O-K-GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DE-O-K-GLUCONATE|molecule.ecocyc.DE-O-K-GLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DE-O-GLUCONATE|molecule.ecocyc.DE-O-GLUCONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:KDUD-RXN`

## Notes

NAD + DE-O-GLUCONATE -> PROTON + NADH + DE-O-K-GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT
