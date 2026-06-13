---
entity_id: "reaction.ecocyc.RXN0-2661"
entity_type: "reaction"
name: "RXN0-2661"
source_database: "EcoCyc"
source_id: "RXN0-2661"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2661

`reaction.ecocyc.RXN0-2661`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2661`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-With-GO-A-Mismatch + WATER -> DNA-containing-abasic-Sites + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-With-GO-A-Mismatch + WATER -> DNA-containing-abasic-Sites + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutY (protein.P17802). Substrates: H2O (molecule.C00001), DNA with adenine:7,8-dihydro-8-oxoguanine mismatch (molecule.ecocyc.DNA-With-GO-A-Mismatch). Products: Adenine (molecule.C00147).

## Annotation

DNA-With-GO-A-Mismatch + WATER -> DNA-containing-abasic-Sites + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P17802|protein.P17802]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-With-GO-A-Mismatch|molecule.ecocyc.DNA-With-GO-A-Mismatch]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2661`

## Notes

DNA-With-GO-A-Mismatch + WATER -> DNA-containing-abasic-Sites + ADENINE; direction=PHYSIOL-LEFT-TO-RIGHT
