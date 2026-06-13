---
entity_id: "reaction.ecocyc.RXN0-4261"
entity_type: "reaction"
name: "RXN0-4261"
source_database: "EcoCyc"
source_id: "RXN0-4261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4261

`reaction.ecocyc.RXN0-4261`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4261`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the processive unwinding of double-stranded DNA to yield single-stranded DNA. EcoCyc reaction equation: Supercoiled-Duplex-DNAs + ATP + WATER -> ADP + Pi + Single-Stranded-DNAs; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the processive unwinding of double-stranded DNA to yield single-stranded DNA.

## Biological Role

Catalyzed by replicative DNA helicase (complex.ecocyc.CPLX0-3621), recD (protein.P04993), dinG (protein.P27296), yoaA (protein.P76257). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Annotation

This reaction is the processive unwinding of double-stranded DNA to yield single-stranded DNA.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3621|complex.ecocyc.CPLX0-3621]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P04993|protein.P04993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27296|protein.P27296]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76257|protein.P76257]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-4261`

## Notes

Supercoiled-Duplex-DNAs + ATP + WATER -> ADP + Pi + Single-Stranded-DNAs; direction=PHYSIOL-LEFT-TO-RIGHT
