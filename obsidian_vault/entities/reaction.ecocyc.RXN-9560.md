---
entity_id: "reaction.ecocyc.RXN-9560"
entity_type: "reaction"
name: "RXN-9560"
source_database: "EcoCyc"
source_id: "RXN-9560"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9560

`reaction.ecocyc.RXN-9560`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9560`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10204 + ACETALD -> CPD-10206 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10204 + ACETALD -> CPD-10206 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Acetaldehyde (molecule.C00084), norfuraneol (molecule.ecocyc.CPD-10204). Products: H2O (molecule.C00001), (2E)-2-ethylidene-4-hydroxy-5-methyl-3(2H)-furanone (molecule.ecocyc.CPD-10206).

## Annotation

CPD-10204 + ACETALD -> CPD-10206 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-10206|molecule.ecocyc.CPD-10206]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10204|molecule.ecocyc.CPD-10204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9560`

## Notes

CPD-10204 + ACETALD -> CPD-10206 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
