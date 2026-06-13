---
entity_id: "reaction.ecocyc.YIAE1-RXN"
entity_type: "reaction"
name: "5-dehydro-D-gluconate 2-dehydrogenase"
source_database: "EcoCyc"
source_id: "YIAE1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5-dehydro-D-gluconate 2-dehydrogenase

`reaction.ecocyc.YIAE1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:YIAE1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an alternative substrate reaction of EC 1.1.1.215. EcoCyc reaction equation: 5-DEHYDROGLUCONATE + NADP -> PROTON + 25-DIDEHYDRO-D-GLUCONATE + NADPH; direction=RIGHT-TO-LEFT. This is an alternative substrate reaction of EC 1.1.1.215.

## Biological Role

Catalyzed by glyoxylate reductase [multifunctional] (complex.ecocyc.CPLX0-235). Substrates: NADP+ (molecule.C00006), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2,5-didehydro-D-gluconate (molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE).

## Enriched Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Annotation

This is an alternative substrate reaction of EC 1.1.1.215.

## Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-235|complex.ecocyc.CPLX0-235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE|molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:YIAE1-RXN`

## Notes

5-DEHYDROGLUCONATE + NADP -> PROTON + 25-DIDEHYDRO-D-GLUCONATE + NADPH; direction=RIGHT-TO-LEFT
