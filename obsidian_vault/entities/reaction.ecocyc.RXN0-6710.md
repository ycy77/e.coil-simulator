---
entity_id: "reaction.ecocyc.RXN0-6710"
entity_type: "reaction"
name: "phosphoribosyl 1,2-cyclic phosphodiesterase"
source_database: "EcoCyc"
source_id: "RXN0-6710"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# phosphoribosyl 1,2-cyclic phosphodiesterase

`reaction.ecocyc.RXN0-6710`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6710`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2463 + WATER -> PROTON + RIBOSE-15-BISPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2463 + WATER -> PROTON + RIBOSE-15-BISPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5-phospho-α-D-ribosyl 1,2-cyclic phosphate phosphodiesterase (complex.ecocyc.CPLX0-7936). Substrates: H2O (molecule.C00001), alpha-D-Ribose 1,2-cyclic phosphate 5-phosphate (molecule.C20440). Products: H+ (molecule.C00080), D-Ribose 1,5-bisphosphate (molecule.C01151).

## Enriched Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)
- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Annotation

CPD0-2463 + WATER -> PROTON + RIBOSE-15-BISPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7805` (aminomethyl)phosphonate degradation (EcoCyc)
- `ecocyc.PWY0-1533` methylphosphonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7936|complex.ecocyc.CPLX0-7936]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01151|molecule.C01151]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20440|molecule.C20440]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6710`

## Notes

CPD0-2463 + WATER -> PROTON + RIBOSE-15-BISPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
