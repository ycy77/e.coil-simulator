---
entity_id: "reaction.ecocyc.RXN-22778"
entity_type: "reaction"
name: "RXN-22778"
source_database: "EcoCyc"
source_id: "RXN-22778"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22778

`reaction.ecocyc.RXN-22778`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22778`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15374 + L-ALPHA-ALANINE -> CPD-25241 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15374 + L-ALPHA-ALANINE -> CPD-25241 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Alanine (molecule.C00041), aldehydo-D-glucose (molecule.ecocyc.CPD-15374). Products: H2O (molecule.C00001), N-(1-deoxy-D-fructos-1-yl)-L-alanine (molecule.ecocyc.CPD-25241).

## Annotation

CPD-15374 + L-ALPHA-ALANINE -> CPD-25241 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-25241|molecule.ecocyc.CPD-25241]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15374|molecule.ecocyc.CPD-15374]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22778`

## Notes

CPD-15374 + L-ALPHA-ALANINE -> CPD-25241 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
