---
entity_id: "reaction.ecocyc.FCLREDUCT-RXN"
entity_type: "reaction"
name: "FCLREDUCT-RXN"
source_database: "EcoCyc"
source_id: "FCLREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FCLREDUCT-RXN

`reaction.ecocyc.FCLREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FCLREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13118 + NADP -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-13118 + NADP -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NADP+ (molecule.C00006), GDP-L-fucose (molecule.C00325). Products: NADPH (molecule.C00005), H+ (molecule.C00080), GDP-4-dehydro-6-deoxy-β-L-galactose (molecule.ecocyc.GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE).

## Enriched Pathways

- `ecocyc.PWY-66` GDP-L-fucose biosynthesis I (from GDP-D-mannose) (EcoCyc)

## Annotation

CPD-13118 + NADP -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-66` GDP-L-fucose biosynthesis I (from GDP-D-mannose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE|molecule.ecocyc.GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00325|molecule.C00325]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FCLREDUCT-RXN`

## Notes

CPD-13118 + NADP -> GDP-4-DEHYDRO-6-L-DEOXYGALACTOSE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
