---
entity_id: "reaction.ecocyc.RXN0-7352"
entity_type: "reaction"
name: "RXN0-7352"
source_database: "EcoCyc"
source_id: "RXN0-7352"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7352

`reaction.ecocyc.RXN0-7352`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7352`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GMP + WATER -> GUANINE + RIBOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GMP + WATER -> GUANINE + RIBOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleotide 5'-monophosphate nucleosidase (complex.ecocyc.CPLX0-8262). Substrates: H2O (molecule.C00001), GMP (molecule.C00144). Products: D-Ribose 5-phosphate (molecule.C00117), Guanine (molecule.C00242).

## Annotation

GMP + WATER -> GUANINE + RIBOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8262|complex.ecocyc.CPLX0-8262]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7352`

## Notes

GMP + WATER -> GUANINE + RIBOSE-5P; direction=PHYSIOL-LEFT-TO-RIGHT
