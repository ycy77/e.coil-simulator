---
entity_id: "reaction.ecocyc.RXN-20680"
entity_type: "reaction"
name: "RXN-20680"
source_database: "EcoCyc"
source_id: "RXN-20680"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20680

`reaction.ecocyc.RXN-20680`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20680`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-gulosides + NAD -> 3-Dehydro-D-gulosides + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-gulosides + NAD -> 3-Dehydro-D-gulosides + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ycjQ (protein.P76043). Substrates: NAD+ (molecule.C00003), a D-guloside (molecule.ecocyc.D-gulosides). Products: NADH (molecule.C00004), H+ (molecule.C00080), a 3-dehydro-D-guloside (molecule.ecocyc.3-Dehydro-D-gulosides).

## Enriched Pathways

- `ecocyc.PWY0-1602` D-gulosides conversion to D-glucosides (EcoCyc)

## Annotation

D-gulosides + NAD -> 3-Dehydro-D-gulosides + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1602` D-gulosides conversion to D-glucosides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76043|protein.P76043]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-Dehydro-D-gulosides|molecule.ecocyc.3-Dehydro-D-gulosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-gulosides|molecule.ecocyc.D-gulosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20680`

## Notes

D-gulosides + NAD -> 3-Dehydro-D-gulosides + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
