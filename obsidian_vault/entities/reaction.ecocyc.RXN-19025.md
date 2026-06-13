---
entity_id: "reaction.ecocyc.RXN-19025"
entity_type: "reaction"
name: "RXN-19025"
source_database: "EcoCyc"
source_id: "RXN-19025"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19025

`reaction.ecocyc.RXN-19025`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19025`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-thymidine-dimer + Light -> DNA-thymidines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-thymidine-dimer + Light -> DNA-thymidines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: hν (molecule.ecocyc.Light). Products: a thymidine in DNA (molecule.ecocyc.DNA-thymidines).

## Annotation

DNA-thymidine-dimer + Light -> DNA-thymidines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.DNA-thymidines|molecule.ecocyc.DNA-thymidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19025`

## Notes

DNA-thymidine-dimer + Light -> DNA-thymidines; direction=PHYSIOL-LEFT-TO-RIGHT
