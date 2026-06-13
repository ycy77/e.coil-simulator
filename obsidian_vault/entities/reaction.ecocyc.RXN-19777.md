---
entity_id: "reaction.ecocyc.RXN-19777"
entity_type: "reaction"
name: "RXN-19777"
source_database: "EcoCyc"
source_id: "RXN-19777"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19777

`reaction.ecocyc.RXN-19777`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19777`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-7249 + HYDROGEN-PEROXIDE -> CPD-7248 + WATER; direction=REVERSIBLE EcoCyc reaction equation: CPD-7249 + HYDROGEN-PEROXIDE -> CPD-7248 + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX). Substrates: Hydrogen peroxide (molecule.C00027), 6-decylubiquinol (molecule.ecocyc.CPD-7249). Products: H2O (molecule.C00001), 6-decylubiquinone (molecule.ecocyc.CPD-7248).

## Annotation

CPD-7249 + HYDROGEN-PEROXIDE -> CPD-7248 + WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7248|molecule.ecocyc.CPD-7248]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-7249|molecule.ecocyc.CPD-7249]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7975|molecule.ecocyc.CPD-7975]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-19777`

## Notes

CPD-7249 + HYDROGEN-PEROXIDE -> CPD-7248 + WATER; direction=REVERSIBLE
