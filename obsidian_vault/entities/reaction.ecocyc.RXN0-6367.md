---
entity_id: "reaction.ecocyc.RXN0-6367"
entity_type: "reaction"
name: "RXN0-6367"
source_database: "EcoCyc"
source_id: "RXN0-6367"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6367

`reaction.ecocyc.RXN0-6367`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6367`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2101 + NADP -> PROTON + CPD-11770 + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD0-2101 + NADP -> PROTON + CPD-11770 + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dihydromonapterin reductase (complex.ecocyc.CPLX0-8571). Substrates: NADP+ (molecule.C00006), 5,6,7,8-Tetrahydromonapterin (molecule.C21007). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 7,8-Dihydromonapterin (molecule.C21008).

## Enriched Pathways

- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Annotation

CPD0-2101 + NADP -> PROTON + CPD-11770 + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8571|complex.ecocyc.CPLX0-8571]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21008|molecule.C21008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C21007|molecule.C21007]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6367`

## Notes

CPD0-2101 + NADP -> PROTON + CPD-11770 + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
