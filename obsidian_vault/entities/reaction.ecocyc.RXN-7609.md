---
entity_id: "reaction.ecocyc.RXN-7609"
entity_type: "reaction"
name: "RXN-7609"
source_database: "EcoCyc"
source_id: "RXN-7609"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7609

`reaction.ecocyc.RXN-7609`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7609`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

GMP + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GMP + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yrfG (protein.P64636). Substrates: H2O (molecule.C00001), GMP (molecule.C00144). Products: Guanosine (molecule.C00387), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)

## Annotation

GMP + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P64636|protein.P64636]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7609`

## Notes

GMP + WATER -> GUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
