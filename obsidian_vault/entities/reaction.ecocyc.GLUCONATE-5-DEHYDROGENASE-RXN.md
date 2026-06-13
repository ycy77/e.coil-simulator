---
entity_id: "reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "GLUCONATE-5-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "GLUCONATE-5-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "5-KETO-D-GLUCONATE 5-REDUCTASE"
---

# GLUCONATE-5-DEHYDROGENASE-RXN

`reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCONATE-5-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + GLUCONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: NAD-P-OR-NOP + GLUCONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by 5-keto-D-gluconate 5-reductase (complex.ecocyc.CPLX0-8292). Substrates: D-Gluconic acid (molecule.C00257), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.IDNCAT-PWY` L-idonate degradation (EcoCyc)

## Annotation

NAD-P-OR-NOP + GLUCONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.IDNCAT-PWY` L-idonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8292|complex.ecocyc.CPLX0-8292]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUCONATE-5-DEHYDROGENASE-RXN`

## Notes

NAD-P-OR-NOP + GLUCONATE -> NADH-P-OR-NOP + 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE
