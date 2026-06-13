---
entity_id: "reaction.ecocyc.RXN0-7385"
entity_type: "reaction"
name: "RXN0-7385"
source_database: "EcoCyc"
source_id: "RXN0-7385"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7385

`reaction.ecocyc.RXN0-7385`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7385`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Quinones + NADPH + PROTON -> Reduced-Quinones + NADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Quinones + NADPH + PROTON -> Reduced-Quinones + NADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADPH-dependent nitroreductase / NADPH-dependent quinone reductase (complex.ecocyc.CPLX0-244). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080), a quinone (molecule.ecocyc.Quinones). Products: NADP+ (molecule.C00006), a quinol (molecule.ecocyc.Reduced-Quinones).

## Annotation

Quinones + NADPH + PROTON -> Reduced-Quinones + NADP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-244|complex.ecocyc.CPLX0-244]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Reduced-Quinones|molecule.ecocyc.Reduced-Quinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Quinones|molecule.ecocyc.Quinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7385`

## Notes

Quinones + NADPH + PROTON -> Reduced-Quinones + NADP; direction=LEFT-TO-RIGHT
