---
entity_id: "reaction.ecocyc.RXN-14161"
entity_type: "reaction"
name: "RXN-14161"
source_database: "EcoCyc"
source_id: "RXN-14161"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14161

`reaction.ecocyc.RXN-14161`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14161`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

DAMP + WATER -> DEOXYADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DAMP + WATER -> DEOXYADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), dCMP phosphohydrolase (complex.ecocyc.CPLX0-7625). Substrates: H2O (molecule.C00001), dAMP (molecule.C00360). Products: Deoxyadenosine (molecule.C00559), phosphate (molecule.ecocyc.Pi).

## Annotation

DAMP + WATER -> DEOXYADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7625|complex.ecocyc.CPLX0-7625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00360|molecule.C00360]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14161`

## Notes

DAMP + WATER -> DEOXYADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
