---
entity_id: "reaction.ecocyc.1.1.1.274-RXN"
entity_type: "reaction"
name: "1.1.1.274-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.274-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2,5-diketo-D-gluconate reductase"
---

# 1.1.1.274-RXN

`reaction.ecocyc.1.1.1.274-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.274-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-377 + NADP -> PROTON + NADPH + 25-DIDEHYDRO-D-GLUCONATE; direction=RIGHT-TO-LEFT EcoCyc reaction equation: CPD-377 + NADP -> PROTON + NADPH + 25-DIDEHYDRO-D-GLUCONATE; direction=RIGHT-TO-LEFT.

## Biological Role

Substrates: NADP+ (molecule.C00006), 2-Keto-D-gluconic acid (molecule.C06473). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2,5-didehydro-D-gluconate (molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE).

## Enriched Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Annotation

CPD-377 + NADP -> PROTON + NADPH + 25-DIDEHYDRO-D-GLUCONATE; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE|molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06473|molecule.C06473]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.274-RXN`

## Notes

CPD-377 + NADP -> PROTON + NADPH + 25-DIDEHYDRO-D-GLUCONATE; direction=RIGHT-TO-LEFT
