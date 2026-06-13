---
entity_id: "reaction.ecocyc.RXN0-7249"
entity_type: "reaction"
name: "RXN0-7249"
source_database: "EcoCyc"
source_id: "RXN0-7249"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7249

`reaction.ecocyc.RXN0-7249`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7249`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

DIHYDROXY-ACETONE-PHOSPHATE + WATER -> DIHYDROXYACETONE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXY-ACETONE-PHOSPHATE + WATER -> DIHYDROXYACETONE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Glycerone phosphate (molecule.C00111). Products: Glycerone (molecule.C00184), phosphate (molecule.ecocyc.Pi).

## Annotation

DIHYDROXY-ACETONE-PHOSPHATE + WATER -> DIHYDROXYACETONE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00184|molecule.C00184]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7249`

## Notes

DIHYDROXY-ACETONE-PHOSPHATE + WATER -> DIHYDROXYACETONE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
