---
entity_id: "reaction.ecocyc.RXN-19778"
entity_type: "reaction"
name: "RXN-19778"
source_database: "EcoCyc"
source_id: "RXN-19778"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19778

`reaction.ecocyc.RXN-19778`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19778`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinols + HYDROGEN-PEROXIDE -> Ubiquinones + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinols + HYDROGEN-PEROXIDE -> Ubiquinones + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX). Substrates: Hydrogen peroxide (molecule.C00027), Ubiquinol (molecule.C00390). Products: H2O (molecule.C00001), a ubiquinone (molecule.ecocyc.Ubiquinones).

## Annotation

Ubiquinols + HYDROGEN-PEROXIDE -> Ubiquinones + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19778`

## Notes

Ubiquinols + HYDROGEN-PEROXIDE -> Ubiquinones + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
