---
entity_id: "reaction.ecocyc.1.1.1.264-RXN"
entity_type: "reaction"
name: "1.1.1.264-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.264-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.264-RXN

`reaction.ecocyc.1.1.1.264-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.264-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + L-IDONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: NAD-P-OR-NOP + L-IDONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by idnD (protein.P39346). Substrates: L-idonate (molecule.ecocyc.L-IDONATE), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.IDNCAT-PWY` L-idonate degradation (EcoCyc)

## Annotation

NAD-P-OR-NOP + L-IDONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.IDNCAT-PWY` L-idonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39346|protein.P39346]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.264-RXN`

## Notes

NAD-P-OR-NOP + L-IDONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE
