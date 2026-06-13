---
entity_id: "reaction.ecocyc.RXN0-7348"
entity_type: "reaction"
name: "RXN0-7348"
source_database: "EcoCyc"
source_id: "RXN0-7348"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7348

`reaction.ecocyc.RXN0-7348`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7348`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL

## Enriched Summary

PHOSPHO-OMPR + WATER -> CPLX0-8285 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-OMPR + WATER -> CPLX0-8285 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1500` EnvZ/OmpR Two-Component Signal Transduction System (EcoCyc)

## Annotation

PHOSPHO-OMPR + WATER -> CPLX0-8285 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1500` EnvZ/OmpR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7348`

## Notes

PHOSPHO-OMPR + WATER -> CPLX0-8285 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
