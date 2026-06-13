---
entity_id: "reaction.ecocyc.THREODEHYD-RXN"
entity_type: "reaction"
name: "THREODEHYD-RXN"
source_database: "EcoCyc"
source_id: "THREODEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THREODEHYD-RXN

`reaction.ecocyc.THREODEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THREODEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the major pathway for threonine utilization in E. coli. EcoCyc reaction equation: THR + NAD -> AMINO-OXOBUT + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in the major pathway for threonine utilization in E. coli.

## Biological Role

Substrates: NAD+ (molecule.C00003), L-Threonine (molecule.C00188). Products: NADH (molecule.C00004), H+ (molecule.C00080), L-2-Amino-3-oxobutanoic acid (molecule.C03508).

## Enriched Pathways

- `ecocyc.THRDLCTCAT-PWY` L-threonine degradation III (to methylglyoxal) (EcoCyc)
- `ecocyc.THREONINE-DEG2-PWY` L-threonine degradation II (EcoCyc)

## Annotation

This is the first reaction in the major pathway for threonine utilization in E. coli.

## Pathways

- `ecocyc.THRDLCTCAT-PWY` L-threonine degradation III (to methylglyoxal) (EcoCyc)
- `ecocyc.THREONINE-DEG2-PWY` L-threonine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03508|molecule.C03508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THREODEHYD-RXN`

## Notes

THR + NAD -> AMINO-OXOBUT + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
