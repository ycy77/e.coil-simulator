---
entity_id: "reaction.ecocyc.L-IDONATE-2-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "L-idonate 2-dehydrogenase"
source_database: "EcoCyc"
source_id: "L-IDONATE-2-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "5-keto-<small>D</small>-gluconate 2-reductase"
  - "<small>L</small>-idonate dehydrogenase"
  - "5-ketogluconate 2-reductase"
  - "reductase, 5-ketogluconate 5- (<small>L</small>-idonate-forming)"
  - "5KGR"
  - "5-ketoglucono-idono-reductase"
---

# L-idonate 2-dehydrogenase

`reaction.ecocyc.L-IDONATE-2-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:L-IDONATE-2-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-IDONATE + NADP -> 5-DEHYDROGLUCONATE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-IDONATE + NADP -> 5-DEHYDROGLUCONATE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NADP+ (molecule.C00006), L-idonate (molecule.ecocyc.L-IDONATE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE).

## Annotation

L-IDONATE + NADP -> 5-DEHYDROGLUCONATE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:L-IDONATE-2-DEHYDROGENASE-RXN`

## Notes

L-IDONATE + NADP -> 5-DEHYDROGLUCONATE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
