---
entity_id: "reaction.ecocyc.RXN-15123"
entity_type: "reaction"
name: "RXN-15123"
source_database: "EcoCyc"
source_id: "RXN-15123"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15123

`reaction.ecocyc.RXN-15123`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15123`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16013 + WATER -> 2-OXOBUTANOATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-16013 + WATER -> 2-OXOBUTANOATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by enamine/imine deaminase, redox-regulated chaperone (complex.ecocyc.CPLX0-1881). Substrates: H2O (molecule.C00001), 2-iminobutanoate (molecule.ecocyc.CPD-16013). Products: 2-Oxobutanoate (molecule.C00109), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)
- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Annotation

CPD-16013 + WATER -> 2-OXOBUTANOATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)
- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1881|complex.ecocyc.CPLX0-1881]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16013|molecule.ecocyc.CPD-16013]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15123`

## Notes

CPD-16013 + WATER -> 2-OXOBUTANOATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
