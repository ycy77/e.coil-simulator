---
entity_id: "reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "RIBITOL-2-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "RIBITOL-2-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBITOL-2-DEHYDROGENASE-RXN

`reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBITOL-2-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RIBITOL + NAD -> D-RIBULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: RIBITOL + NAD -> D-RIBULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), Ribitol (molecule.C00474). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Ribulose (molecule.C00309).

## Enriched Pathways

- `ecocyc.RIBITOLUTIL-PWY` ribitol degradation I (EcoCyc)

## Annotation

RIBITOL + NAD -> D-RIBULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.RIBITOLUTIL-PWY` ribitol degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00309|molecule.C00309]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00474|molecule.C00474]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBITOL-2-DEHYDROGENASE-RXN`

## Notes

RIBITOL + NAD -> D-RIBULOSE + NADH + PROTON; direction=LEFT-TO-RIGHT
