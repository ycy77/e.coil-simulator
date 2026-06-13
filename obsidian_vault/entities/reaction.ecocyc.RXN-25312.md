---
entity_id: "reaction.ecocyc.RXN-25312"
entity_type: "reaction"
name: "RXN-25312"
source_database: "EcoCyc"
source_id: "RXN-25312"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25312

`reaction.ecocyc.RXN-25312`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25312`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9117 + WATER -> PHENOL + D-galactopyranose; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9117 + WATER -> PHENOL + D-galactopyranose; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX). Substrates: H2O (molecule.C00001), phenyl-β-galactoside (molecule.ecocyc.CPD-9117). Products: D-Galactose (molecule.C00124), Phenol (molecule.C00146).

## Annotation

CPD-9117 + WATER -> PHENOL + D-galactopyranose; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00146|molecule.C00146]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9117|molecule.ecocyc.CPD-9117]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25312`

## Notes

CPD-9117 + WATER -> PHENOL + D-galactopyranose; direction=LEFT-TO-RIGHT
