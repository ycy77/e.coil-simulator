---
entity_id: "reaction.ecocyc.3.1.21.7-RXN"
entity_type: "reaction"
name: "3.1.21.7-RXN"
source_database: "EcoCyc"
source_id: "3.1.21.7-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Escherichia coli endodeoxyribonuclease V"
---

# 3.1.21.7-RXN

`reaction.ecocyc.3.1.21.7-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.21.7-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-containing-abasic-Sites + WATER -> Deoxy-Ribonucleoside-Monophosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-containing-abasic-Sites + WATER -> Deoxy-Ribonucleoside-Monophosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a 2'-deoxyribonucleoside 5'-monophosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates).

## Annotation

DNA-containing-abasic-Sites + WATER -> Deoxy-Ribonucleoside-Monophosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.21.7-RXN`

## Notes

DNA-containing-abasic-Sites + WATER -> Deoxy-Ribonucleoside-Monophosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
