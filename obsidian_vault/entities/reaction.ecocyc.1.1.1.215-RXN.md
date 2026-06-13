---
entity_id: "reaction.ecocyc.1.1.1.215-RXN"
entity_type: "reaction"
name: "1.1.1.215-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.215-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2-KETO-D-GLUCONATE REDUCTASE"
---

# 1.1.1.215-RXN

`reaction.ecocyc.1.1.1.215-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.215-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADP + GLUCONATE -> PROTON + CPD-377 + NADPH; direction=RIGHT-TO-LEFT EcoCyc reaction equation: NADP + GLUCONATE -> PROTON + CPD-377 + NADPH; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by glyoxylate reductase [multifunctional] (complex.ecocyc.CPLX0-235). Substrates: NADP+ (molecule.C00006), D-Gluconic acid (molecule.C00257). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-Keto-D-gluconic acid (molecule.C06473).

## Enriched Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Annotation

NADP + GLUCONATE -> PROTON + CPD-377 + NADPH; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-235|complex.ecocyc.CPLX0-235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06473|molecule.C06473]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.215-RXN`

## Notes

NADP + GLUCONATE -> PROTON + CPD-377 + NADPH; direction=RIGHT-TO-LEFT
