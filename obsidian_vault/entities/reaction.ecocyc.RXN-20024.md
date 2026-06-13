---
entity_id: "reaction.ecocyc.RXN-20024"
entity_type: "reaction"
name: "RXN-20024"
source_database: "EcoCyc"
source_id: "RXN-20024"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20024

`reaction.ecocyc.RXN-20024`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20024`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-21612 + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21612 + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), iron(III)-[(2,3-dihydroxybenzoylserine)2] complex (molecule.ecocyc.CPD-21612). Products: iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine] complex (molecule.ecocyc.CPD-17082), N-(2,3-dihydroxybenzoyl)-L-serine (molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE).

## Annotation

CPD-21612 + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.ecocyc.CPD-17082|molecule.ecocyc.CPD-17082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE|molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21612|molecule.ecocyc.CPD-21612]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20024`

## Notes

CPD-21612 + WATER + PROTON -> CPD-17082 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT
