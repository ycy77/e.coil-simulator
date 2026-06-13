---
entity_id: "reaction.ecocyc.RXN0-7339"
entity_type: "reaction"
name: "RXN0-7339"
source_database: "EcoCyc"
source_id: "RXN0-7339"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7339

`reaction.ecocyc.RXN0-7339`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7339`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL

## Enriched Summary

PHOSPHO-BASR + WATER -> BASR-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-BASR + WATER -> BASR-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by basS (protein.P30844). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1482` BasSR Two-Component Signal Transduction System (EcoCyc)

## Annotation

PHOSPHO-BASR + WATER -> BASR-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1482` BasSR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P30844|protein.P30844]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7339`

## Notes

PHOSPHO-BASR + WATER -> BASR-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
