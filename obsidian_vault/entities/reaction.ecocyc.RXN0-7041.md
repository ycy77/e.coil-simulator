---
entity_id: "reaction.ecocyc.RXN0-7041"
entity_type: "reaction"
name: "RXN0-7041"
source_database: "EcoCyc"
source_id: "RXN0-7041"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7041

`reaction.ecocyc.RXN0-7041`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7041`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

THIAMINE-PYROPHOSPHATE + Pi + PROTON -> CPD-611 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THIAMINE-PYROPHOSPHATE + Pi + PROTON -> CPD-611 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX). Substrates: Thiamin diphosphate (molecule.C00068), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi). Products: H2O (molecule.C00001), H+ (molecule.C00080), Thiamin triphosphate (molecule.C03028).

## Annotation

THIAMINE-PYROPHOSPHATE + Pi + PROTON -> CPD-611 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03028|molecule.C03028]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7041`

## Notes

THIAMINE-PYROPHOSPHATE + Pi + PROTON -> CPD-611 + WATER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
