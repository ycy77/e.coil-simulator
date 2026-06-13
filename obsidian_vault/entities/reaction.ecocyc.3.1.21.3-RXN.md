---
entity_id: "reaction.ecocyc.3.1.21.3-RXN"
entity_type: "reaction"
name: "3.1.21.3-RXN"
source_database: "EcoCyc"
source_id: "3.1.21.3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Type I restriction enzyme"
---

# 3.1.21.3-RXN

`reaction.ecocyc.3.1.21.3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.21.3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Double-Stranded-DNAs + WATER -> Double-Stranded-DNA-with-terminal-PO4s + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Double-Stranded-DNAs + WATER -> Double-Stranded-DNA-with-terminal-PO4s + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by EcoKI restriction-modification system (complex.ecocyc.CPLX0-3958). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + Double-Stranded-DNAs + WATER -> Double-Stranded-DNA-with-terminal-PO4s + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3958|complex.ecocyc.CPLX0-3958]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.21.3-RXN`

## Notes

ATP + Double-Stranded-DNAs + WATER -> Double-Stranded-DNA-with-terminal-PO4s + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
