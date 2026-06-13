---
entity_id: "reaction.ecocyc.RXN0-5387"
entity_type: "reaction"
name: "RXN0-5387"
source_database: "EcoCyc"
source_id: "RXN0-5387"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5387

`reaction.ecocyc.RXN0-5387`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5387`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1156 + NADPH + PROTON -> CPD0-1157 + NADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1156 + NADPH + PROTON -> CPD0-1157 + NADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by qorB (protein.P39315). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080), 2-methyl-1,4-benzoquinone (molecule.ecocyc.CPD0-1156). Products: NADP+ (molecule.C00006), methyl-1,4-benzoquinol (molecule.ecocyc.CPD0-1157).

## Annotation

CPD0-1156 + NADPH + PROTON -> CPD0-1157 + NADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39315|protein.P39315]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1157|molecule.ecocyc.CPD0-1157]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1156|molecule.ecocyc.CPD0-1156]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5387`

## Notes

CPD0-1156 + NADPH + PROTON -> CPD0-1157 + NADP; direction=PHYSIOL-LEFT-TO-RIGHT
