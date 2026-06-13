---
entity_id: "reaction.ecocyc.RXN0-313"
entity_type: "reaction"
name: "RXN0-313"
source_database: "EcoCyc"
source_id: "RXN0-313"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-313

`reaction.ecocyc.RXN0-313`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-313`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FRUCTOSE-6P -> DIHYDROXYACETONE + GAP; direction=REVERSIBLE EcoCyc reaction equation: FRUCTOSE-6P -> DIHYDROXYACETONE + GAP; direction=REVERSIBLE.

## Biological Role

Catalyzed by fructose-6-phosphate aldolase 1 (complex.ecocyc.CPLX0-201), fructose-6-phosphate aldolase 2 (complex.ecocyc.CPLX0-8584). Substrates: β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P). Products: D-Glyceraldehyde 3-phosphate (molecule.C00118), Glycerone (molecule.C00184).

## Annotation

FRUCTOSE-6P -> DIHYDROXYACETONE + GAP; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-201|complex.ecocyc.CPLX0-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8584|complex.ecocyc.CPLX0-8584]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00184|molecule.C00184]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01112|molecule.C01112]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-15826|molecule.ecocyc.CPD-15826]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8879|molecule.ecocyc.CPD-8879]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-313`

## Notes

FRUCTOSE-6P -> DIHYDROXYACETONE + GAP; direction=REVERSIBLE
