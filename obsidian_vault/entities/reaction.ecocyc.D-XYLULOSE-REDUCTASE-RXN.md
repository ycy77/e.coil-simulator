---
entity_id: "reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN"
entity_type: "reaction"
name: "D-XYLULOSE-REDUCTASE-RXN"
source_database: "EcoCyc"
source_id: "D-XYLULOSE-REDUCTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-XYLULOSE-REDUCTASE-RXN

`reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:D-XYLULOSE-REDUCTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

XYLITOL + NAD -> D-XYLULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: XYLITOL + NAD -> D-XYLULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), Xylitol (molecule.C00379). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Xylulose (molecule.C00310).

## Enriched Pathways

- `ecocyc.LARABITOLUTIL-PWY` xylitol degradation I (EcoCyc)

## Annotation

XYLITOL + NAD -> D-XYLULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.LARABITOLUTIL-PWY` xylitol degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00310|molecule.C00310]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00379|molecule.C00379]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:D-XYLULOSE-REDUCTASE-RXN`

## Notes

XYLITOL + NAD -> D-XYLULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT
