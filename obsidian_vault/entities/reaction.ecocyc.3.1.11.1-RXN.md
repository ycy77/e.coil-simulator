---
entity_id: "reaction.ecocyc.3.1.11.1-RXN"
entity_type: "reaction"
name: "3.1.11.1-RXN"
source_database: "EcoCyc"
source_id: "3.1.11.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Exonuclease I"
  - "E.coli exonuclease I"
---

# 3.1.11.1-RXN

`reaction.ecocyc.3.1.11.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.11.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-N + WATER -> DNA-N + Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-N + WATER -> DNA-N + Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sbcB (protein.P04995), tatD (protein.P27859), yhbQ (protein.P45472). Substrates: H2O (molecule.C00001). Products: a 2'-deoxyribonucleoside 5'-monophosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates).

## Annotation

DNA-N + WATER -> DNA-N + Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P04995|protein.P04995]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27859|protein.P27859]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P45472|protein.P45472]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.11.1-RXN`

## Notes

DNA-N + WATER -> DNA-N + Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
