---
entity_id: "reaction.ecocyc.RXN0-300"
entity_type: "reaction"
name: "hydroxypyruvate reductase (NADP+)"
source_database: "EcoCyc"
source_id: "RXN0-300"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hydroxypyruvate reductase (NADP+)

`reaction.ecocyc.RXN0-300`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-300`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCERATE + NADP -> PROTON + OH-PYR + NADPH; direction=RIGHT-TO-LEFT EcoCyc reaction equation: GLYCERATE + NADP -> PROTON + OH-PYR + NADPH; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by glyoxylate reductase [multifunctional] (complex.ecocyc.CPLX0-235), ghrA (protein.P75913). Substrates: NADP+ (molecule.C00006), D-Glycerate (molecule.C00258). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Hydroxypyruvate (molecule.C00168).

## Annotation

GLYCERATE + NADP -> PROTON + OH-PYR + NADPH; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-235|complex.ecocyc.CPLX0-235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75913|protein.P75913]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-300`

## Notes

GLYCERATE + NADP -> PROTON + OH-PYR + NADPH; direction=RIGHT-TO-LEFT
