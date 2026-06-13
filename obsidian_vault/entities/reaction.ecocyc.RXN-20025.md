---
entity_id: "reaction.ecocyc.RXN-20025"
entity_type: "reaction"
name: "RXN-20025"
source_database: "EcoCyc"
source_id: "RXN-20025"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20025

`reaction.ecocyc.RXN-20025`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20025`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FERRIC-ENTEROBACTIN-COMPLEX + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FERRIC-ENTEROBACTIN-COMPLEX + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fes (protein.P13039). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Fe-enterobactin (molecule.C06230). Products: iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine] complex (molecule.ecocyc.CPD-17082), N-(2,3-dihydroxybenzoyl)-L-serine (molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE).

## Annotation

FERRIC-ENTEROBACTIN-COMPLEX + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P13039|protein.P13039]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-17082|molecule.ecocyc.CPD-17082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE|molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20025`

## Notes

FERRIC-ENTEROBACTIN-COMPLEX + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT
