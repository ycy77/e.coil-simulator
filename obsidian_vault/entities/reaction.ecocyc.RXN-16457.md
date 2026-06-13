---
entity_id: "reaction.ecocyc.RXN-16457"
entity_type: "reaction"
name: "RXN-16457"
source_database: "EcoCyc"
source_id: "RXN-16457"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16457

`reaction.ecocyc.RXN-16457`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16457`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15870 + CPD-4 + PROTON -> CPD-15874 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15870 + CPD-4 + PROTON -> CPD-15874 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Molybdopterin (molecule.C05924), Molybdoenzyme molybdenum cofactor (molecule.C18237). Products: H2O (molecule.C00001), bis(molybdenum cofactor) (molecule.ecocyc.CPD-15874).

## Enriched Pathways

- `ecocyc.PWY-7639` bis(guanylyl molybdenum cofactor) biosynthesis (EcoCyc)

## Annotation

CPD-15870 + CPD-4 + PROTON -> CPD-15874 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7639` bis(guanylyl molybdenum cofactor) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15874|molecule.ecocyc.CPD-15874]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05924|molecule.C05924]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16457`

## Notes

CPD-15870 + CPD-4 + PROTON -> CPD-15874 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
