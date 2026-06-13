---
entity_id: "reaction.ecocyc.RXN-9311"
entity_type: "reaction"
name: "RXN-9311"
source_database: "EcoCyc"
source_id: "RXN-9311"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9311

`reaction.ecocyc.RXN-9311`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9311`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9925 + WATER -> PROTON + DIHYDROXYNAPHTHOATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9925 + WATER -> PROTON + DIHYDROXYNAPHTHOATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 1,4-dihydroxy-2-naphthoyl-CoA hydrolase (complex.ecocyc.CPLX0-8128). Substrates: H2O (molecule.C00001), 1,4-Dihydroxy-2-naphthoyl-CoA (molecule.C15547). Products: CoA (molecule.C00010), H+ (molecule.C00080), 1,4-Dihydroxy-2-naphthoate (molecule.C03657).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Annotation

CPD-9925 + WATER -> PROTON + DIHYDROXYNAPHTHOATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8128|complex.ecocyc.CPLX0-8128]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03657|molecule.C03657]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15547|molecule.C15547]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9311`

## Notes

CPD-9925 + WATER -> PROTON + DIHYDROXYNAPHTHOATE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
