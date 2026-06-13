---
entity_id: "reaction.ecocyc.RXN-19026"
entity_type: "reaction"
name: "RXN-19026"
source_database: "EcoCyc"
source_id: "RXN-19026"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19026

`reaction.ecocyc.RXN-19026`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19026`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-deoxycytidine-dimer + Light -> DNA-Cytidines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-deoxycytidine-dimer + Light -> DNA-Cytidines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: hν (molecule.ecocyc.Light). Products: a 2'-deoxycytidine in DNA (molecule.ecocyc.DNA-Cytidines).

## Annotation

DNA-deoxycytidine-dimer + Light -> DNA-Cytidines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.DNA-Cytidines|molecule.ecocyc.DNA-Cytidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19026`

## Notes

DNA-deoxycytidine-dimer + Light -> DNA-Cytidines; direction=PHYSIOL-LEFT-TO-RIGHT
