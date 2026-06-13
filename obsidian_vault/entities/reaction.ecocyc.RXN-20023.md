---
entity_id: "reaction.ecocyc.RXN-20023"
entity_type: "reaction"
name: "RXN-20023"
source_database: "EcoCyc"
source_id: "RXN-20023"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20023

`reaction.ecocyc.RXN-20023`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20023`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2482 + WATER + PROTON -> CPD-21612 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2482 + WATER + PROTON -> CPD-21612 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine trimer] complex (molecule.ecocyc.CPD0-2482). Products: iron(III)-[(2,3-dihydroxybenzoylserine)2] complex (molecule.ecocyc.CPD-21612), N-(2,3-dihydroxybenzoyl)-L-serine (molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE).

## Annotation

CPD0-2482 + WATER + PROTON -> CPD-21612 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.ecocyc.CPD-21612|molecule.ecocyc.CPD-21612]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE|molecule.ecocyc.N-23-DIHYDROXYBENZOYL-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2482|molecule.ecocyc.CPD0-2482]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20023`

## Notes

CPD0-2482 + WATER + PROTON -> CPD-21612 + N-23-DIHYDROXYBENZOYL-L-SERINE; direction=PHYSIOL-LEFT-TO-RIGHT
