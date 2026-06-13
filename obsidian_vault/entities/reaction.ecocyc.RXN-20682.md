---
entity_id: "reaction.ecocyc.RXN-20682"
entity_type: "reaction"
name: "RXN-20682"
source_database: "EcoCyc"
source_id: "RXN-20682"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20682

`reaction.ecocyc.RXN-20682`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20682`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glucosides + NAD -> 3-Dehydro-D-Glucosides + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Glucosides + NAD -> 3-Dehydro-D-Glucosides + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ycjS (protein.P77503). Substrates: NAD+ (molecule.C00003), D-Glucoside (molecule.C01798). Products: NADH (molecule.C00004), H+ (molecule.C00080), a 3-dehydro-D-glucoside (molecule.ecocyc.3-Dehydro-D-Glucosides).

## Enriched Pathways

- `ecocyc.PWY0-1602` D-gulosides conversion to D-glucosides (EcoCyc)

## Annotation

Glucosides + NAD -> 3-Dehydro-D-Glucosides + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-1602` D-gulosides conversion to D-glucosides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77503|protein.P77503]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-Dehydro-D-Glucosides|molecule.ecocyc.3-Dehydro-D-Glucosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01798|molecule.C01798]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20682`

## Notes

Glucosides + NAD -> 3-Dehydro-D-Glucosides + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
