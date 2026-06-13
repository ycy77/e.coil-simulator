---
entity_id: "reaction.ecocyc.RXN-9524"
entity_type: "reaction"
name: "3-oxo-octanoyl-[acyl-carrier protein] reductase"
source_database: "EcoCyc"
source_id: "RXN-9524"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-oxo-octanoyl-[acyl-carrier protein] reductase

`reaction.ecocyc.RXN-9524`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9524`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Hydroxy-octanoyl-ACPs + NADP -> 3-Oxo-octanoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: 3-Hydroxy-octanoyl-ACPs + NADP -> 3-Oxo-octanoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

3-Hydroxy-octanoyl-ACPs + NADP -> 3-Oxo-octanoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9524`

## Notes

3-Hydroxy-octanoyl-ACPs + NADP -> 3-Oxo-octanoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
