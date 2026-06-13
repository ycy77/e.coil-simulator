---
entity_id: "reaction.ecocyc.RXN0-7020"
entity_type: "reaction"
name: "RXN0-7020"
source_database: "EcoCyc"
source_id: "RXN0-7020"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7020

`reaction.ecocyc.RXN0-7020`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7020`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13059 + NADP -> 25-DIDEHYDRO-D-GLUCONATE + NADPH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: CPD-13059 + NADP -> 25-DIDEHYDRO-D-GLUCONATE + NADPH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dkgB (protein.P30863), dkgA (protein.Q46857). Substrates: NADP+ (molecule.C00006), 2-keto-L-gulonate (molecule.ecocyc.CPD-13059). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2,5-didehydro-D-gluconate (molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE).

## Enriched Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Annotation

CPD-13059 + NADP -> 25-DIDEHYDRO-D-GLUCONATE + NADPH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P30863|protein.P30863]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46857|protein.Q46857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE|molecule.ecocyc.25-DIDEHYDRO-D-GLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13059|molecule.ecocyc.CPD-13059]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7020`

## Notes

CPD-13059 + NADP -> 25-DIDEHYDRO-D-GLUCONATE + NADPH + PROTON; direction=RIGHT-TO-LEFT
