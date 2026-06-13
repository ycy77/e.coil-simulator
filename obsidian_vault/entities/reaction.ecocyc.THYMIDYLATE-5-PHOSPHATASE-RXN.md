---
entity_id: "reaction.ecocyc.THYMIDYLATE-5-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "THYMIDYLATE-5-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "THYMIDYLATE-5-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THYMIDYLATE-5-PHOSPHATASE-RXN

`reaction.ecocyc.THYMIDYLATE-5-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THYMIDYLATE-5-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + TMP -> Pi + THYMIDINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + TMP -> Pi + THYMIDINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), dTMP (molecule.C00364). Products: Thymidine (molecule.C00214), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + TMP -> Pi + THYMIDINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00364|molecule.C00364]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THYMIDYLATE-5-PHOSPHATASE-RXN`

## Notes

WATER + TMP -> Pi + THYMIDINE; direction=PHYSIOL-LEFT-TO-RIGHT
