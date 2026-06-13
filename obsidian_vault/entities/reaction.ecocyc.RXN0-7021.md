---
entity_id: "reaction.ecocyc.RXN0-7021"
entity_type: "reaction"
name: "L-idonate 2-dehydrogenase"
source_database: "EcoCyc"
source_id: "RXN0-7021"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-idonate 2-dehydrogenase

`reaction.ecocyc.RXN0-7021`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7021`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-IDONATE + NADP -> CPD-13059 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: L-IDONATE + NADP -> CPD-13059 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by glyoxylate reductase [multifunctional] (complex.ecocyc.CPLX0-235). Substrates: NADP+ (molecule.C00006), L-idonate (molecule.ecocyc.L-IDONATE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-keto-L-gulonate (molecule.ecocyc.CPD-13059).

## Enriched Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Annotation

L-IDONATE + NADP -> CPD-13059 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.KETOGLUCONMET-PWY` ketogluconate metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-235|complex.ecocyc.CPLX0-235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13059|molecule.ecocyc.CPD-13059]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7021`

## Notes

L-IDONATE + NADP -> CPD-13059 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
